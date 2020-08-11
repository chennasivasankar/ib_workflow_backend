"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
from typing import Dict, List


class GetSheetDataForTaskCreationConfig:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_task_creation_config_sub_sheet(self):
        from ib_tasks.constants.constants import TASK_CREATION_CONFIG_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            sub_sheet_name=TASK_CREATION_CONFIG_SUB_SHEET
        )
        self._validation_for_task_creation_config_dict(field_records)
        tasks_dict = [
            self._convert_task_creation_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records
        ]
        from ib_tasks.populate.populate_task_initial_stage_actions_logic import \
            populate_tasks
        populate_tasks(tasks_dict)

    def _validation_for_task_creation_config_dict(self, tasks_dict: List[Dict]):
        from schema import Schema, Optional, SchemaError
        schema = Schema(
            [{
                "TaskTemplate ID*": str,
                "Stage ID*": str,
                "Stage Display Name": str,
                "Action name": str,
                "Role": str,
                "Logic": str,
                "Button Text": str,
                Optional("Button Colour"): str,
                Optional("Action Type"): str,
                Optional("Transition Template ID"): str
            }],
            ignore_extra_keys=True
        )
        try:
            schema.validate(tasks_dict)
        except SchemaError:
            self._raise_exception_for_valid_task_creation_format()

    @staticmethod
    def _convert_task_creation_sheet_data_dict_to_our_format(
            field_record: Dict):
        return {
            "task_template_id": field_record["TaskTemplate ID*"],
            "stage_id": field_record["Stage ID*"],
            "action_logic": field_record["Logic"],
            "action_name": field_record["Action name"],
            "roles": field_record["Role"],
            "button_text": field_record["Button Text"],
            "button_color": field_record["Button Colour"],
            "action_type": field_record["Action Type"],
            "transition_template_id": field_record["Transition Template ID"]
        }

    def _raise_exception_for_valid_task_creation_format(self):
        valid_format = {
            "TaskTemplate ID*": "FIN_PR",
            "Stage ID*": "PR_PAYMENT_REQUEST_DRAFTS",
            "Stage Display Name": "Payment Request Drafts",
            "Stage Display Logic": "Value [Status1]== Value[PR_PAYMENT_REQUEST_DRAFTS]",
            "Action name": "Save Draft",
            "Role": "ALL_ROLES",
            "Logic": "Status1 = PR_PAYMENT_REQUEST_DRAFTS",
            "Button Text": "Save Draft",
            "Button Colour": "Blue"

        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)
