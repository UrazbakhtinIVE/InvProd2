from django.test import TestCase
from django.db.models.signals import pre_save

from printers.models import PrinterType, PrinterModel, \
    PrinterStatus, Printer, PrinterScheduler
from mainapp.models import Category, Firm
from printers.signals import update_scheduler_status_from_printer


def create_test_data():
    """Создание данных для тестов."""
    Category.objects.create(name="категория 1", slug="categorya-1")
    Firm.objects.create(name="xerox", slug="xerox")
    PrinterStatus.objects.create(name="работает", slug="rabotaet")
    PrinterStatus.objects.create(name="не работает", slug="ne-rabotaet")

    PrinterType.objects.create(name="лазерный", slug="lazerny")
    PrinterModel.objects.create(category_id=1, firm_id=1,
                                printerType_id=1, name="модель 1")
    Printer.objects.create(serialNumber="123", printerModel_id=1,
                           status_id=1, name="принтер 1", ip="123")


class PrinterSignalsTestCase(TestCase):
    """Тестирование обработчика update_scheduler_status_from_printer
     сигнала post_save для модели Printer."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Установка неизменяемых на протяжении теста данных."""
        create_test_data()

    def test_connection(self) -> None:
        """Тестирование успешного подключения сигнала."""
        is_disconnected = pre_save.disconnect(
            receiver=update_scheduler_status_from_printer, sender=Printer)
        self.assertTrue(is_disconnected)
        pre_save.connect(receiver=update_scheduler_status_from_printer, sender=Printer)

    def test_new_scheduler_instance(self) -> None:
        """Тестирование создания нового экземпляра PrinterScheduler и
        установку ему соответствующих атрибутов на основе экземпляра Printer."""
        printer_instance = Printer.objects.get(pk=1)

        printer_instance.status_id = 2
        printer_instance.save()

        scheduler_instance = PrinterScheduler.objects.get(pk=1)

        self.assertIsInstance(scheduler_instance, PrinterScheduler)
        self.assertEqual(scheduler_instance.printer, printer_instance)
        self.assertEqual(scheduler_instance.printerStatus, printer_instance.status)
        self.assertEqual(scheduler_instance.location, printer_instance.location)

    def test_printer_should_update_scheduler_status(self) -> None:
        """Тестирование создания нового экземпляра PrinterScheduler и
        установку ему соответствующего статуса на основе экземпляра Printer."""
        printer_instance = Printer.objects.get(pk=1)
        previuos_printer_status = printer_instance.status

        printer_instance.status = PrinterStatus.objects.get(pk=2)
        printer_instance.save()

        scheduler_instance = PrinterScheduler.objects.get(pk=1)
        self.assertNotEqual(scheduler_instance.printerStatus, previuos_printer_status)
        self.assertNotEqual(printer_instance.status, previuos_printer_status)