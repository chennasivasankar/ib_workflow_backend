import factory

from ib_boards.models import Board, Column, ColumnPermission, UserStarredBoard


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class UserStarredBoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserStarredBoard

    user_id = factory.Sequence(lambda n: f'user_id_{n}')
    board_id = factory.SubFactory(BoardFactory)


class ColumnFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Column

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    name = factory.Sequence(
        lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    display_order = factory.Sequence(lambda n: n + 1)
    task_selection_config = """
        {
            "FIN_PR":["stage_id_1", "stage_id_2", "stage_id_3"]
        }
    """
    list_brief_view_config = """
        {
            "FIN_PR":["PR_PAYMENT_REQUEST_DRAFTS"]
        }
    """
    kanban_brief_view_config = """
        {
            "FIN_PR":["PR_PAYMENT_REQUEST_DRAFTS"]
        }
    """
    board = factory.SubFactory(BoardFactory)


class ColumnPermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ColumnPermission

    column = factory.SubFactory(ColumnFactory)
    user_role_id = 'ALL_ROLES'
