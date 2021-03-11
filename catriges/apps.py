from django.apps import AppConfig


class CatrigesConfig(AppConfig):
    name = 'catriges'

    def ready(self):
        from . import signals


