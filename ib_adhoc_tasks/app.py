from django.apps import AppConfig


class IbAdhocTasksAppConfig(AppConfig):
    name = "ib_adhoc_tasks"

    def ready(self):
        from ib_adhoc_tasks import signals # pylint: disable=unused-variable
