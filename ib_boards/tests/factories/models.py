import factory

from ib_boards.models import Board, Column


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class ColumnFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Column

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    display_name = factory.Sequence(
        lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    display_order = factory.Sequence(lambda n: n + 1)
    task_selection_config = """
        {
            FIN_PR:[PR_PAYMENT_REQUEST_DRAFTS]
        }
    """
    list_view_fields = """
        {
            FIN_PR:[PR_PAYMENT_REQUEST_DRAFTS]
        }
    """
    kanban_view_fields = """
        {
            FIN_PR:[PR_PAYMENT_REQUEST_DRAFTS]
        }
    """
    board_id = "BOARD_ID_0"


class ColumnPermission(factory.django.DjangoModelFactory):
    column = ColumnFactory()
    user_role_id = ['ALL_ROLES']