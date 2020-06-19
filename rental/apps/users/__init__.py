from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    name = 'rental.apps.users'
    label = 'users'
    verbose_name = 'Users'

    def ready(self):
        import rental.apps.users.signals

default_app_config = 'rental.apps.users.UsersAppConfig'