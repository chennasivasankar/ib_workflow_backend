"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""


class GetDataFromSheet:

    @staticmethod
    def get_data_from_sub_sheet(spread_sheet_name: str, sub_sheet_name: str):
        from ib_boards.utils.read_google_sheet import read_google_sheet
        sheet = read_google_sheet(sheet_name=spread_sheet_name)
        fields_config_sheet = sheet.worksheet(sub_sheet_name)
        field_records = fields_config_sheet.get_all_records()
        return field_records

    @staticmethod
    def raise_exception_for_valid_format(valid_format):
        import json
        json_valid_format = json.dumps(valid_format, indent=4)
        from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board import \
            InvalidDataFormat
        raise InvalidDataFormat(valid_format=json_valid_format)
