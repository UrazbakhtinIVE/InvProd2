from django.apps import AppConfig


class PrintersConfig(AppConfig):
    name = 'printers'

    def ready(self):
        from . import signals