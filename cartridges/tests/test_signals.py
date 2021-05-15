from django.test import TestCase
from django.db.models.signals import pre_save

from cartridges.models import CartridgeModel, Cartridge, CartridgeScheduler
from mainapp.models import Category, Firm
from cartridges.signals import update_scheduler_status_from_cartridge


def create_test_data():
    """Создание данных для тестов."""
    Category.objects.create(name="категория 1", slug="categorya-1")
    Firm.objects.create(name="xerox", slug="xerox")

    CartridgeModel.objects.create(category_id=1, firm_id=1, name="модель 1")
    Cartridge.objects.create(serialNumber="123", cartridgeModel_id=1)


class CartridgesSignalsTestCase(TestCase):
    """Тестирование обработчика update_scheduler_status_from_cartridge
     сигнала post_save для модели Cartridge."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Установка неизменяемых на протяжении теста данных."""
        create_test_data()

    def test_connection(self) -> None:
        """Тестирование успешного подключения сигнала."""
        is_disconnected = pre_save.disconnect(
            receiver=update_scheduler_status_from_cartridge, sender=Cartridge)
        self.assertTrue(is_disconnected)
        pre_save.connect(receiver=update_scheduler_status_from_cartridge, sender=Cartridge)

    def test_new_scheduler_instance(self) -> None:
        """Тестирование создания нового экземпляра CartridgeScheduler и
        установку ему соответствующих атрибутов на основе экземпляра Cartridge."""
        cartridge_instance = Cartridge.objects.get(pk=1)

        cartridge_instance.status = "working"
        cartridge_instance.save()

        scheduler_instance = CartridgeScheduler.objects.get(pk=1)

        self.assertIsInstance(scheduler_instance, CartridgeScheduler)
        self.assertEqual(scheduler_instance.cartridge, cartridge_instance)
        self.assertEqual(scheduler_instance.cartridgeStatus, cartridge_instance.status)

    def test_cartridge_should_update_scheduler_status(self) -> None:
        """Тестирование создания нового экземпляра CartridgeScheduler и
        установку ему соответсвующего статуса на основе экземпляра Cartridge."""
        cartridge_instance = Cartridge.objects.get(pk=1)
        previuos_cartridge_status = cartridge_instance.status

        cartridge_instance.status = "working"
        cartridge_instance.save()

        scheduler_instance = CartridgeScheduler.objects.get(pk=1)
        self.assertNotEqual(scheduler_instance.cartridgeStatus, previuos_cartridge_status)
        self.assertNotEqual(cartridge_instance.status, previuos_cartridge_status)