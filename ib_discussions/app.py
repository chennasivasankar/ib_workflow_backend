from django.apps import AppConfig


class IbDiscussionsAppConfig(AppConfig):
    name = "ib_discussions"

    def ready(self):
        from ib_discussions import signals # pylint: disable=unused-variable
