"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
from typing import Dict, List


class GetSheetDataForStages:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_stage_id_and_values_sub_sheet(self):
        from ib_tasks.constants.constants import STAGE_ID_AND_VALUES_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            sub_sheet_name=STAGE_ID_AND_VALUES_SUB_SHEET
        )
        # TODO need to remove list slicing
        self._validation_for_stages_dict(field_records[:2])
        stages_dict = [
            self._convert_stages_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records[:2]
        ]
        from ib_tasks.populate.create_or_update_stages import \
            populate_stages_values
        populate_stages_values(list_of_stages_dict=stages_dict)

    @staticmethod
    def _convert_stages_sheet_data_dict_to_our_format(field_record: Dict):
        return {
            "task_template_id": field_record["TaskTemplate ID*"],
            "stage_id": field_record["Stage ID*"],
            "value": field_record["Value"],
            "stage_display_name": field_record["Stage Display Name"],
            "stage_display_logic": field_record["Stage Display Logic"]
        }

    def _validation_for_stages_dict(self, actions_dict: List[Dict]):
        from schema import Schema, SchemaError
        from schema import And
        schema = Schema(
            [{
                "TaskTemplate ID*": And(str, len),
                "Stage ID*": And(str, len),
                "Stage Display Name": str,
                "Value": int,
                "Stage Display Logic": And(str, len)
            }]
        )
        try:
            schema.validate(actions_dict)
        except SchemaError:
            self._raise_exception_for_valid_stage_format()

    def _raise_exception_for_valid_stage_format(self):
        valid_format = {
            "TaskTemplate ID*": "FIN_PR",
            "Stage ID*": "PR_PAYMENT_REQUEST_DRAFTS",
            "Stage Display Name": "Payment Request Drafts",
            "Value": 1,
            "Stage Display Logic": "Status1==PR_PAYMENT_REQUEST_DRAFTS"
        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)
