"""
Created on: 22/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Dict


class GetSheetDataForStageActions:

    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_stages_and_actions_sub_sheet(self):
        from ib_tasks.constants.constants import STAGES_AND_ACTIONS_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            sub_sheet_name=STAGES_AND_ACTIONS_SUB_SHEET
        )

        self._validation_for_action_dict(field_records)
        stage_actions_dict = [
            self._convert_stage_action_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records
        ]
        from ib_tasks.populate.populate_stage_actions import \
            populate_stage_actions
        populate_stage_actions(stage_actions_dict)

    @staticmethod
    def _convert_stage_action_sheet_data_dict_to_our_format(field_record: Dict):
        return {
            "stage_id": field_record["Stage ID*"],
            "action_logic": field_record["Logic"],
            "action_name": field_record["Action name"],
            "roles": field_record["Role"],
            "button_text": field_record["Button Text"],
            "button_color": field_record["Button Colour"],
            "action_type": field_record["Action Type"],
            "transition_template_id": field_record["Transition Template ID"]
        }

    def _validation_for_action_dict(self, actions_dict: List[Dict]):
        from schema import Schema, Optional, SchemaError
        from schema import And
        schema = Schema(
            [{
                "Stage ID*": And(str, len),
                "Stage Display Logic": And(str, len),
                "Action name": And(str, len),
                "Role": And(str, len),
                "Logic": And(str, len),
                "Button Text": And(str, len),
                Optional("Button Colour"): str,
                Optional("Action Type"): str,
                Optional("Transition Template ID"): str

            }]
        )
        try:
            schema.validate(actions_dict)
        except SchemaError:
            self._raise_exception_for_valid_stage_actions_format()

    def _raise_exception_for_valid_stage_actions_format(self):
        valid_format = {
            "Stage ID*": "PR_PAYMENT_REQUEST_DRAFTS",
            "Stage Display Logic": "Value [Status1] == Value[PR_PAYMENT_REQUEST_DRAFTS]",
            "Action name": "Save Draft",
            "Role": "ALL_ROLES",
            "Logic": "Status1 = PR_PAYMENT_REQUEST_DRAFTS",
            "Button Text": "Save Draft",
            "Button Colour": "Blue",
            "Transition Template ID": "transition_template_id",
            "Action Type": "NO VALIDATIONS"

        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)

