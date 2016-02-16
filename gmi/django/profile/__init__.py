from django.apps import AppConfig


class ProfileApp(AppConfig):
    name = 'gmi.django.profile'

    def ready(self):
        import gmi.django.profile.signals
