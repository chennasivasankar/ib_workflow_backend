from django.apps import AppConfig

class IbIamAppConfig(AppConfig):
    name = "ib_iam"

    def ready(self):
        from ib_iam import signals # pylint: disable=unused-variable
