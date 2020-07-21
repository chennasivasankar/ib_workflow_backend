"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""


class GetBoardsAndColumnsDataFromSheet:

    @staticmethod
    def get_data_from_sheet():
        from ib_boards.populate.read_google_sheet import read_google_sheet
        from ib_boards.constants.constants import \
            GOOGLE_SHEET_NAME, FIELD_SUB_SHEET_TITLE
        sheet = read_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
        fields_config_sheet = sheet.worksheet(FIELD_SUB_SHEET_TITLE)
        field_records = fields_config_sheet.get_all_records()
        from ib_boards.populate.populate_script_to_create_boards_and_columns\
            import PopulateCreateBoardsAndColumns

        populate_script = PopulateCreateBoardsAndColumns()
        populate_script.populate_create_boards_and_columns(
            boards_columns_dicts=field_records
        )
