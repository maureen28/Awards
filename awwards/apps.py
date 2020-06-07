from django.apps import AppConfig


class AwwardsConfig(AppConfig):
    name = 'awwards'

    def ready(self):
        import awwards.signals