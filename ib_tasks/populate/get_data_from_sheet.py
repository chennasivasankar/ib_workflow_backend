

class GetDataFromSheet:

    @staticmethod
    def get_data_from_sub_sheet(sub_sheet_name: str):
        from ib_tasks.utils.get_google_sheet import get_google_sheet
        from ib_tasks.constants.constants import \
            GOOGLE_SHEET_NAME
        sheet = get_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
        fields_config_sheet = sheet.worksheet(sub_sheet_name)
        field_records = fields_config_sheet.get_all_records()
        return field_records

    @staticmethod
    def raise_exception_for_valid_format(valid_format):
        import json
        json_valid_format = json.dumps(valid_format, indent=4)
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidFormatException
        raise InvalidFormatException(valid_format=json_valid_format)

