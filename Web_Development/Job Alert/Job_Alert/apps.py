from django.apps import AppConfig


class JobAlertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Job_Alert'

    def ready(self):
        import Job_Alert.signals