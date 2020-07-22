"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
from typing import Dict, List


class PopulateStageActionsAndTaskCreationConfig:

    @staticmethod
    def _get_data_from_sub_sheet(sub_sheet_name: str):
        from ib_tasks.populate.read_google_sheet import read_google_sheet
        from ib_tasks.constants.constants import \
            GOOGLE_SHEET_NAME
        sheet = read_google_sheet(sheet_name=GOOGLE_SHEET_NAME)
        fields_config_sheet = sheet.worksheet(sub_sheet_name)
        field_records = fields_config_sheet.get_all_records()
        return field_records

    def get_data_from_stages_and_actions_sub_sheet(self):
        from ib_tasks.constants.constants import STAGES_AND_ACTIONS_SUB_SHEET
        field_records = self._get_data_from_sub_sheet(
            sub_sheet_name=STAGES_AND_ACTIONS_SUB_SHEET
        )
        self._validation_for_action_dict(field_records)
        stage_actions_dict = [
            self._convert_stage_action_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records[:4]
        ]
        from ib_tasks.populate.populate_stage_actions import \
            populate_stage_actions
        populate_stage_actions(stage_actions_dict)

    def get_data_from_task_creation_config_sub_sheet(self):
        from ib_tasks.constants.constants import TASK_CREATION_CONFIG_SUB_SHEET
        field_records = self._get_data_from_sub_sheet(
            sub_sheet_name=TASK_CREATION_CONFIG_SUB_SHEET
        )
        import json
        print(json.dumps(field_records, indent=4))
        self._validation_for_task_creation_config_dict(field_records)
        tasks_dict = [
            self._convert_task_creation_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records[:4]
        ]
        from ib_tasks.populate.populate_task_initial_stage_actions_logic import \
            populate_tasks
        populate_tasks(tasks_dict)

    @staticmethod
    def _convert_stage_action_sheet_data_dict_to_our_format(field_record: Dict):
        return {
            "stage_id": field_record["Stage ID*"],
            "action_logic": "\ta = '9'",
            "action_name": field_record["Action name"],
            "roles": field_record["Role"],
            "button_text": field_record["Button Text"],
            "button_color": field_record["Button Colour"]
        }

    def _convert_task_creation_sheet_data_dict_to_our_format(
            self, field_record: Dict):
        task_dict = self._convert_stage_action_sheet_data_dict_to_our_format(
            field_record
        )
        task_dict.update(
            {
                "task_template_id": field_record["TaskTemplate ID*"]
            }
        )
        return task_dict

    def _validation_for_action_dict(self, actions_dict: List[Dict]):
        from schema import Schema, Optional, SchemaError
        schema = Schema(
            [{
                "Stage ID*": str,
                "Stage Display Name": str,
                "Stage Display Logic": str,
                "Action name": str,
                "Role": str,
                "Logic": str,
                "Button Text": str,
                Optional("Button Colour"): str

            }]
        )
        try:
            schema.validate(actions_dict)
        except SchemaError:
            self._raise_exception_for_valid_format()

    def _validation_for_task_creation_config_dict(self, tasks_dict: List[Dict]):
        from schema import Schema, Optional, SchemaError
        schema = Schema(
            [{
                "TaskTemplate ID": str,
                "Stage ID*": str,
                "Stage Display Name": str,
                "Action name": str,
                "Role": str,
                "Logic": str,
                "Button Text": str,
                Optional("Button Colour"): str

            }]
        )
        try:
            schema.validate(tasks_dict)
        except SchemaError:
            self._raise_exception_for_valid_task_creation_format()

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
        self._raise_exception_for_valid_format(valid_format)

    def _raise_exception_for_valid_stage_actions_format(self):
        valid_format = {
            "Stage ID*": "PR_PAYMENT_REQUEST_DRAFTS",
            "Stage Display Name": "Payment Request Drafts",
            "Stage Display Logic": "Value [Status1]== Value[PR_PAYMENT_REQUEST_DRAFTS]",
            "Action name": "Save Draft",
            "Role": "ALL_ROLES",
            "Logic": "Status1 = PR_PAYMENT_REQUEST_DRAFTS",
            "Button Text": "Save Draft",
            "Button Colour": "Blue"

        }
        self._raise_exception_for_valid_format(valid_format)

    @staticmethod
    def _raise_exception_for_valid_format(valid_format):
        import json
        json_valid_format = json.dumps(valid_format, indent=4)
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidFormatException
        raise InvalidFormatException(valid_format=json_valid_format)

