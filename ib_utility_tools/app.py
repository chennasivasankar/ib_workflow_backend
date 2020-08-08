from django.apps import AppConfig


class IbUtilityToolsAppConfig(AppConfig):
    name = "ib_utility_tools"

    def ready(self):
        from ib_utility_tools import signals # pylint: disable=unused-variable
