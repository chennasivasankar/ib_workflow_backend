"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import json
from typing import List, Dict

from ib_boards.interactors.dtos import ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO
from ib_boards.tests.factories.interactor_dtos import \
    TaskTemplateStagesDTOFactory, TaskSummaryFieldsDTOFactory


class InvalidDataFormat(Exception):
    pass


class StorageImplementation(object):
    pass


class InvalidJsonFormat(Exception):
    pass


class PopulateAddOrDeleteColumnsForBoard:

    def populate_add_or_delete_for_columns_for_board(
            self, boards_columns_dicts: List[Dict]):
        self.validate_keys_in_given_dict(
            boards_columns_dicts=boards_columns_dicts
        )
        column_dtos = self.get_column_dtos_from_dict(boards_columns_dicts)
        from ib_boards.interactors.add_or_delete_columns_for_board_interactor \
            import AddOrDeleteColumnsForBoardInteractor
        storage = StorageImplementation()
        interactor = AddOrDeleteColumnsForBoardInteractor(
            storage=storage
        )
        interactor.add_or_delete_columns_for_board_wrapper(
            column_dtos=column_dtos
        )

    def get_column_dtos_from_dict(self, boards_columns_dicts: List[Dict]):
        column_dtos = [
            self._convert_column_dict_to_column_dto(
                column_dict=column_dict
            )
            for column_dict in boards_columns_dicts
        ]
        return column_dtos

    def _convert_column_dict_to_column_dto(self,
                                           column_dict: Dict) -> ColumnDTO:
        # task_template_stages = self._get_task_template_stages_dto(
        #     column_dict['Task Template Stages that are visible in columns']
        # )
        # list_view_fields = self._get_task_template_summary_fields_dto(
        #     column_dict['Card Info_List']
        # )
        # kanban_view_fields = self._get_task_template_summary_fields_dto(
        #     column_dict['Card Info_Kanban']
        # )
        return ColumnDTO(
            column_id=column_dict['Column ID*'],
            display_name=column_dict['Column Display Name'],
            display_order=column_dict['Column Order For Display'],
            task_template_stages=TaskTemplateStagesDTOFactory.create_batch(3),
            user_role_ids=column_dict['Visible to RoleIDs'],
            column_summary="COLUMN SUMMARY",
            column_actions="COLUMN ACTIONS",
            list_view_fields=TaskSummaryFieldsDTOFactory.create_batch(3),
            kanban_view_fields=TaskSummaryFieldsDTOFactory.create_batch(3),
            board_id=column_dict['Board ID*'],
        )

    def validate_keys_in_given_dict(self, boards_columns_dicts: List[Dict]):
        from schema import Schema, SchemaError
        schema = Schema(
            [{
                "Board ID*": str,
                "Board Display Name": str,
                "Column Order For Display": int,
                "Column ID*": str,
                "Column Display Name": str,
                "Task Template Stages that are visible in columns": str,
                "Visible to RoleIDs": str,
                "Column Summary": str,
                "Column Actions": str,
                "Card Info_Kanban": str,
                "Card Info_List": str


            }]
        )
        try:
            schema.validate(boards_columns_dicts)
        except SchemaError:
            self._raise_exception_for_invalid_data_format()

    def _raise_exception_for_invalid_data_format(self):
        raise InvalidDataFormat("""{
                "Board ID*": str,
                "Board Display Name": str,
                "Column Order For Display": int,
                "Column ID*": str,
                "Column Display Name": str,
                "Task Template Stages that are visible in columns": str,
                "Visible to RoleIDs": [str],
                "Column Summary": str,
                "Column Actions": str,
                "Card Info_Kanban": str,
                "Card Info_List": str
        }""")

    @staticmethod
    def _get_task_template_stages_dto(json_object: json):
        try:
            template_stages = json.loads(json_object)
        except json.JSONDecodeError:
            raise InvalidJsonFormat
        template_stages_dtos = [
            TaskTemplateStagesDTO(
                task_template_id=key,
                stages=value
            )
            for key, value in template_stages.items()
        ]
        return template_stages_dtos

    @staticmethod
    def _get_task_template_summary_fields_dto(json_object: json):
        try:
            task_summary_fields = json.loads(json_object)
        except json.JSONDecodeError:
            raise InvalidJsonFormat
        task_summary_fields = [
            TaskSummaryFieldsDTO(
                task_id=key,
                summary_fields=value
            )
            for key, value in task_summary_fields.items()
        ]
        return task_summary_fields
