from import_export import resources, fields, widgets
from printers.models import Printer


class PrinterAnalyticsResource(resources.ModelResource):
    serialNumber = fields.Field(
        'serialNumber',
        column_name='Серийный номер'
    )
    name = fields.Field(
        'printerModel__name',
        column_name='Название'
    )
    location = fields.Field(
        'location__number',
        column_name='Месторасположение'
    )
    date_of_last_diagnostics = fields.Field(
        'date_of_last_diagnostics',
        column_name='Дата последней диагностики'
    )
    date_of_planned_diagnostics = fields.Field(
        'date_of_planned_diagnostics',
        column_name='Дата плановой диагностики'
    )
    period_of_product_diagnostics = fields.Field(column_name='Период диагностики (дней)')
    days_remain_to_diagnostics = fields.Field(column_name='Дней до плановой диагностики',)

    def dehydrate_period_of_product_diagnostics(self, obj):
        return obj.period_of_product_diagnostics.period.days

    def dehydrate_days_remain_to_diagnostics(self, obj):
        return obj.days_remain_to_diagnostics.days

    def get_queryset(self):
        queryset = super().get_queryset()
        return (printer for printer in queryset if printer.is_need_in_diagnostics)

    class Meta:
        model = Printer
        exclude = ('id', 'person', 'number', 'description',
                   'printerModel', 'ip', 'status',
                   'black_cartridge', 'blue_cartridge', 'yellow_cartridge', 'purple_cartridge')