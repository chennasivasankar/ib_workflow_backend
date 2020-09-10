import factory

from ib_boards.constants.enum import DisplayStatus
from ib_boards.models import Board, Column, ColumnPermission, UserStarredBoard, \
    FieldDisplayStatus, FieldOrder


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    project_id = factory.Sequence(lambda n: f'PROJECT_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class UserStarredBoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserStarredBoard

    user_id = factory.Sequence(lambda n: f'user_id_{n}')
    board = factory.SubFactory(BoardFactory)


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


class FieldDisplayStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FieldDisplayStatus

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    user_id = factory.Sequence(lambda n: f'user_id_{n}')
    field_id = factory.Sequence(lambda n: f'field_id_{n}')
    display_status = DisplayStatus.HIDE.value


class FieldOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FieldOrder

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    user_id = factory.Sequence(lambda n: f'user_id_{n}')
    fields_order = """{
        "field_ids": [
            "field_id_0", "field_id_1", "field_id_2"
        ]
    }"""
