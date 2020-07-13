from django.apps import AppConfig


class IbBoardsAppConfig(AppConfig):
    name = "ib_boards"

    def ready(self):
        from ib_boards import signals # pylint: disable=unused-variable
