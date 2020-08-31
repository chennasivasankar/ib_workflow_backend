from django.db import transaction

from ib_boards.populate.get_data_from_sheet_for_boards_and_columns import \
    GetBoardsAndColumnsDataFromSheet

from ib_boards.populate.get_data_from_sheet_for_project_boards import \
    GetSheetDataForProjectBoards


@transaction.atomic()
def populate_data(**kwargs):
    boards_and_columns = GetBoardsAndColumnsDataFromSheet()
    boards_and_columns.create_boards_and_columns(
        kwargs['boards_columns_spread_sheet_name'])

    project_boards = GetSheetDataForProjectBoards()
    project_boards.get_data_from_project_boards_sub_sheet(
        kwargs['project_boards_spread_sheet_name'])
