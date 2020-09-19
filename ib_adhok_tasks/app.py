from django.apps import AppConfig


class IbAdhok-tasksAppConfig(AppConfig):
    name = "ib_adhok_tasks"

    def ready(self):
        from ib_adhok-tasks import signals # pylint: disable=unused-variable
