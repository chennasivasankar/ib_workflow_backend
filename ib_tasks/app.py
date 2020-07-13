from django.apps import AppConfig


class IbTasksAppConfig(AppConfig):
    name = "ib_tasks"

    def ready(self):
        from ib_tasks import signals # pylint: disable=unused-variable
