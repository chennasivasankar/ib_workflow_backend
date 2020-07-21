"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""


class PopulateStageActions:

    def get_data_from_sheet(self):
        from ib_tasks.populate.read_google_sheet import read_google_sheet
        from ib_tasks.constants.constants import \
            GOOGLE_SHEET_NAME, FIELD_SUB_SHEET_TITLE
        sheet = read_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
        fields_config_sheet = sheet.worksheet(FIELD_SUB_SHEET_TITLE)
        field_records = fields_config_sheet.get_all_records()
        stage_actions_dict = self._conver_sheet_data_dict_to_our_format(
            field_records
        )
        import json
        print(json.dumps(field_records, indent=4))

    def _conver_sheet_data_dict_to_our_format(self, field_records):
        pass
