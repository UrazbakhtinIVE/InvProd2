from django.apps import AppConfig


class CartridgesConfig(AppConfig):
    name = 'cartridges'

    def ready(self):
        from . import signals


