from django.apps import AppConfig


class OutputsConfig(AppConfig):
    name = 'outputs'

    def ready(self):
        from . import signals


