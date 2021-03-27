from django.test import TestCase
from django.db.models.signals import pre_save

from catriges.models import CartridgeModel, Catrige, CatrigeScheduler
from mainapp.models import Category, Firm
from catriges.signals import update_scheduler_status_from_catrige


def create_test_data():
    """Создание данных для тестов."""
    Category.objects.create(name="категория 1", slug="categorya-1")
    Firm.objects.create(name="xerox", slug="xerox")

    CartridgeModel.objects.create(category_id=1, firm_id=1, name="модель 1")
    Catrige.objects.create(serialNumber="123", catrigeModel_id=1)


class CartridgesSignalsTestCase(TestCase):
    """Тестирование обработчика update_scheduler_status_from_catrige
     сигнала post_save для модели Catrige."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Установка неизменяемых на протяжении теста данных."""
        create_test_data()

    def test_connection(self) -> None:
        """Тестирование успешного подключения сигнала."""
        is_disconnected = pre_save.disconnect(
            receiver=update_scheduler_status_from_catrige, sender=Catrige)
        self.assertTrue(is_disconnected)
        pre_save.connect(receiver=update_scheduler_status_from_catrige, sender=Catrige)

    def test_new_scheduler_instance(self) -> None:
        """Тестирование создания нового экземпляра CatrigeScheduler и
        установку ему соответствующих атрибутов на основе экземпляра Catrige."""
        cartridge_instance = Catrige.objects.get(pk=1)

        cartridge_instance.status = "working"
        cartridge_instance.save()

        scheduler_instance = CatrigeScheduler.objects.get(pk=1)

        self.assertIsInstance(scheduler_instance, CatrigeScheduler)
        self.assertEqual(scheduler_instance.catrige, cartridge_instance)
        self.assertEqual(scheduler_instance.catrigeStatus, cartridge_instance.status)

    def test_cartridge_should_update_scheduler_status(self) -> None:
        """Тестирование создания нового экземпляра CatrigeScheduler и
        установку ему соответсвующего статуса на основе экземпляра Catrige."""
        cartridge_instance = Catrige.objects.get(pk=1)
        previuos_cartridge_status = cartridge_instance.status

        cartridge_instance.status = "working"
        cartridge_instance.save()

        scheduler_instance = CatrigeScheduler.objects.get(pk=1)
        self.assertNotEqual(scheduler_instance.catrigeStatus, previuos_cartridge_status)
        self.assertNotEqual(cartridge_instance.status, previuos_cartridge_status)