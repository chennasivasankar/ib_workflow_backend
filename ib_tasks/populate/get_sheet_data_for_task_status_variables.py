"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
from typing import Dict, List


class GetSheetDataForStatusVariables:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_status_variables_sub_sheet(self):
        from ib_tasks.constants.constants import STATUS_VARIABLES_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            sub_sheet_name=STATUS_VARIABLES_SUB_SHEET
        )
        import json
        print(json.dumps(field_records, indent=4))
        self._validation_for_status_variables_dict(field_records)
        list_of_status_dict = [
            self._convert_status_variables_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records
        ]
        from ib_tasks.populate.create_task_status_variables import \
            populate_status_variables
        populate_status_variables(list_of_status_dict=list_of_status_dict)

    @staticmethod
    def _convert_status_variables_sheet_data_dict_to_our_format(
            field_record: Dict):
        return {
            "task_template_id": field_record["Task Template ID"],
            "status_variable_id": field_record["Status Variable ID"]
        }

    def _validation_for_status_variables_dict(self, actions_dict: List[Dict]):
        from schema import Schema, SchemaError
        schema = Schema(
            [{
                "Task Template ID": str,
                "Status Variable ID": str

            }]
        )
        schema.validate(actions_dict)
        try:
            schema.validate(actions_dict)
        except SchemaError:
            self._raise_exception_for_valid_status_variables_format()

    def _raise_exception_for_valid_status_variables_format(self):
        valid_format = {
            "Task Template ID": "FIN_PR",
            "Status Variable ID": "Status1"

        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)
