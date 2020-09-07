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

    def get_data_from_stage_flows_sub_sheet(self, spread_sheet_name: str):
        from ib_tasks.constants.constants import STAGE_FLOWS_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=STAGE_FLOWS_SUB_SHEET
        )
        self._validation_for_stage_flows(field_records)
        stage_flow_dicts = [
            self._convert_stage_flow_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records
        ]
        from ib_tasks.populate.populate_stage_flows import populate_stage_flows
        populate_stage_flows(stage_flow_dicts=stage_flow_dicts)

    @staticmethod
    def _convert_stage_flow_sheet_data_dict_to_our_format(field_record: Dict):

        return {
            "previous_stage_id": field_record["Previous Stage ID*"],
            "action_name": field_record["Action name"],
            "next_stage_id": field_record["Next Stage ID*"]
        }

    def _validation_for_stage_flows(self, stage_flows: List[Dict]):
        from schema import Schema, SchemaError
        from schema import And
        schema = Schema(
            [{
                "Previous Stage ID*": And(str, len),
                "Action name": And(str, len),
                "Next Stage ID*": And(str, len)
            }],
            ignore_extra_keys=True
        )
        try:
            schema.validate(stage_flows)
        except SchemaError:
            self._raise_exception_for_valid_stage_flows_format()

    def _raise_exception_for_valid_stage_flows_format(self):
        valid_format = {
            "Previous Stage ID*": "PREVIOUS STAGE ID",
            "Action name": "SUBMIT",
            "Next Stage ID*": "NEXT STAGE ID"
        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)

