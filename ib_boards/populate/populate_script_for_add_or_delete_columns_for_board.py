"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
import json
from typing import List, Dict

from ib_boards.interactors.dtos import ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO


class InvalidDataFormat(Exception):
    def __init__(self, valid_format):
        self.valid_format = valid_format

    def __str__(self):
        return "Valid Format:" + " " + self.valid_format


class InvalidJsonFormat(Exception):
    pass


class PopulateAddOrDeleteColumnsForBoard:

    def populate_add_or_delete_for_columns_for_board(
            self, boards_columns_dicts: List[Dict]):
        self.validate_keys_in_given_dict(
            boards_columns_dicts=boards_columns_dicts
        )
        column_dtos = self.get_column_dtos_from_dict(boards_columns_dicts)
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        from ib_boards.interactors.add_or_delete_columns_for_board_interactor import \
            AddOrDeleteColumnsForBoardInteractor
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
        task_template_stages = self._get_task_template_stages_dto(
            column_dict['task_template_stages']
        )
        list_view_fields = self._get_task_template_summary_fields_dto(
            column_dict['list_view_fields']
        )
        kanban_view_fields = self._get_task_template_summary_fields_dto(
            column_dict['kanban_view_fields']
        )
        user_role_ids = self._convert_user_role_to_list_from_string(
            user_roles=column_dict['user_role_ids'])
        return ColumnDTO(
            column_id=column_dict['column_id'],
            display_name=column_dict['column_display_name'],
            display_order=column_dict['display_order'],
            task_template_stages=task_template_stages,
            user_role_ids=user_role_ids,
            column_summary=column_dict['column_summary'],
            column_actions=column_dict['column_actions'],
            list_view_fields=list_view_fields,
            kanban_view_fields=kanban_view_fields,
            board_id=column_dict['board_id']
        )

    def validate_keys_in_given_dict(self, boards_columns_dicts: List[Dict]):
        from schema import Schema, SchemaError, Optional
        schema = Schema(
            [{
                "board_id": str,
                "board_display_name": str,
                "column_display_name": str,
                "column_id": str,
                "display_order": int,
                "user_role_ids": str,
                Optional("column_summary"): str,
                Optional("column_actions"): str,
                "task_template_stages": str,
                "kanban_view_fields": str,
                "list_view_fields": str
            }]
        )
        try:
            schema.validate(boards_columns_dicts)
        except SchemaError:
            self._raise_exception_for_board_valid_format()

    @staticmethod
    def _raise_exception_for_board_valid_format():
        valid_format = {
            "board_id": "board_id",
            "board_display_name": "board_display_name",
            "column_id": "column_id",
            "column_display_name": "column_display_name",
            "display_order": "display_order",
            "user_role_ids": "user_role_ids",
            "column_summary": "column_summary",
            "column_actions": "column_actions",
            "task_template_stages": "task_template_stages",
            "kanban_view_fields": "kanban_view_fields",
            "list_view_fields": "list_view_fields"
        }
        import json
        json_valid_format = json.dumps(valid_format, indent=4)
        raise InvalidDataFormat(valid_format=json_valid_format)

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

    @staticmethod
    def _convert_user_role_to_list_from_string(user_roles: str):
        user_roles = user_roles.replace(" ", "")
        user_roles = user_roles.split(",")
        return user_roles
