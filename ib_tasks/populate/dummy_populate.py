from typing import List, Dict

from ib_tasks.interactors.stages_dtos import StageDTO


class Populate:
    @property
    def data_sheet(self):
        from ib_tasks.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_stage_id_and_values_sub_sheet(self,
                                                    spread_sheet_name: str):
        from ib_tasks.constants.constants import STAGE_ID_AND_VALUES_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
                spread_sheet_name=spread_sheet_name,
                sub_sheet_name=STAGE_ID_AND_VALUES_SUB_SHEET
        )

        self._validation_for_stages_dict(field_records)
        stages_dtos = [
                self._convert_to_dto(
                        field_record
                )
                for field_record in field_records
        ]
        self.populate_stages_values(stages_dtos)

    def populate_stages_values(self, stage_dtos: List[StageDTO]):
        from ib_tasks.interactors.create_or_update_stages \
            import CreateOrUpdateStagesInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        interactor = CreateOrUpdateStagesInteractor(
                stage_storage=StagesStorageImplementation(),
                task_storage=TasksStorageImplementation(),
                task_template_storage=TaskTemplateStorageImplementation()
        )
        interactor.create_or_update_stages(stages_details=stage_dtos)

    @staticmethod
    def _convert_to_dto(field_record: Dict):
        return StageDTO(
                task_template_id=field_record["TaskTemplate ID*"],
                stage_id=field_record["Stage ID*"],
                value=field_record["Value"],
                card_info_kanban=field_record["Card Info_Kanban"],
                card_info_list=field_record["Card Info_List"],
                stage_display_name=field_record["Stage Display Name"],
                stage_display_logic=field_record["Stage Display Logic"],
                roles=field_record["Roles"],
                stage_color=field_record["Stage Color"]
        )

    def _validation_for_stages_dict(self, actions_dict: List[Dict]):
        from schema import Schema, SchemaError
        from schema import And
        schema = Schema(
                [{
                        "TaskTemplate ID*": And(str, len),
                        "Stage ID*": And(str, len),
                        "Stage Display Name": str,
                        "Card Info_Kanban": str,
                        "Card Info_List": str,
                        "Value": int,
                        "Stage Display Logic": str,
                        "Roles": str,
                        "Stage Color": str
                }],
                ignore_extra_keys=True
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
                "Card Info_Kanban": ["FIN_FIRST_NAME"],
                "Card Info_List": ["FIN_FIRST_NAME"],
                "Value": 1,
                "Stage Display Logic": "Status1==PR_PAYMENT_REQUEST_DRAFTS",
                "roles": "ALL_ROLES\nFIN_PAYMENT_REQUESTER",
        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)
