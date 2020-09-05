from abc import ABC
from typing import List

from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_boards.adapters.iam_service import InvalidProjectIdsException
from ib_boards.constants.exception_messages import (
    INVALID_BOARD_ID, INVALID_OFFSET_VALUE, INVALID_LIMIT_VALUE,
    USER_DONOT_HAVE_ACCESS, INVALID_PROJECT_ID, USER_IS_NOT_IN_PROJECT)
from ib_boards.interactors.dtos import ColumnTasksDTO, FieldDTO, ActionDTO, \
    StarredAndOtherBoardsDTO, TaskStageDTO, StageAssigneesDTO, AssigneesDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetBoardsPresenterInterface, \
    GetColumnTasksPresenterInterface, TaskCompleteDetailsDTO, TaskDisplayIdDTO, \
    CompleteTasksDetailsDTO, GetColumnTasksListViewPresenterInterface, \
    FieldsDisplayStatusPresenterInterface, FieldsDisplayOrderPresenterInterface
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import ColumnCompleteDetails, \
    AllFieldsDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO)


class GetBoardsPresenterImplementation(GetBoardsPresenterInterface, HTTPResponseMixin):

    def get_response_for_user_have_no_access_for_boards(
            self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_BOARDS
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_BOARDS[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_BOARDS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_offset(self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_limit(self) -> response.HttpResponse:
        from ib_boards.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_get_boards(
            self, starred_and_other_boards_dto: StarredAndOtherBoardsDTO,
            total_boards: int) \
            -> response.HttpResponse:
        board_details_dict = {
            "total_boards_count": total_boards,
            "starred_boards": [],
            "all_boards": []
        }
        for starred_boards_dto in starred_and_other_boards_dto.starred_boards_dtos:
            board_dict = self._convert_board_dto_to_dict(board_dto=starred_boards_dto)
            board_details_dict["starred_boards"].append(board_dict)

        for other_boards_dto in starred_and_other_boards_dto.other_boards_dtos:
            board_dict = self._convert_board_dto_to_dict(board_dto=other_boards_dto)
            board_details_dict["all_boards"].append(board_dict)
        return self.prepare_200_success_response(
            response_dict=board_details_dict
        )

    @staticmethod
    def _convert_board_dto_to_dict(board_dto):
        return {
            "board_id": board_dto.board_id,
            "name": board_dto.name
        }

    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    def get_response_for_invalid_project_id(self, error: InvalidProjectIdsException)\
            -> response.HttpResponse:
        invalid_project_id = error.invalid_project_ids[0]
        response_dict = {
            "response": INVALID_PROJECT_ID[0].format(invalid_project_id),
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_user_is_not_in_project(self) \
            -> response.HttpResponse:
        response_dict = {
            "response": USER_IS_NOT_IN_PROJECT[0],
            "http_status_code": 403,
            "res_status": USER_IS_NOT_IN_PROJECT[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )


class GetColumnTasksPresenterImplementation(GetColumnTasksPresenterInterface,
                                            HTTPResponseMixin):

    def get_response_for_the_invalid_column_id(self):
        from ib_boards.constants.exception_messages import INVALID_COLUMN_ID
        response_dict = {
            "response": INVALID_COLUMN_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_COLUMN_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_stage_ids(self, error):
        pass

    def get_response_column_tasks(
            self, task_complete_details_dto: List[TaskCompleteDetailsDTO],
            total_tasks: int) -> response.HttpResponse:
        pass

    def get_response_for_invalid_offset(self):
        from ib_boards.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_limit(self):
        from ib_boards.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    def get_response_for_user_have_no_access_for_column(self):
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_column_tasks(
            self, complete_tasks_details_dto: CompleteTasksDetailsDTO):
        response_dict = self.get_column_tasks_details(
            complete_tasks_details_dto=complete_tasks_details_dto
        )
        return self.prepare_200_success_response(response_dict)

    def get_column_tasks_details(
            self, complete_tasks_details_dto: CompleteTasksDetailsDTO):

        task_fields_dtos = complete_tasks_details_dto.task_fields_dtos
        task_actions_dtos = complete_tasks_details_dto.task_actions_dtos
        total_tasks = complete_tasks_details_dto.total_tasks
        task_id_dtos = complete_tasks_details_dto.task_id_dtos
        task_stage_dtos = complete_tasks_details_dto.task_stage_dtos
        assignees_dtos = complete_tasks_details_dto.assignees_dtos

        task_ids = [
            task_id_dto.task_id
            for task_id_dto in task_id_dtos
        ]
        task_ids_map = {}
        for task_id_dto in task_id_dtos:
            task_ids_map[task_id_dto.task_id] = task_id_dto.display_id

        task_ids_with_duplicates = task_ids

        task_ids = []
        for task_id in task_ids_with_duplicates:
            if task_id not in task_ids:
                task_ids.append(task_id)

        task_stage_map = {}
        for task_stage_dto in task_stage_dtos:
            task_stage_map[
                task_stage_dto.task_id] = task_stage_dto

        tasks_list = self.get_task_details_dict_from_dtos(
            task_fields_dtos=task_fields_dtos,
            task_actions_dtos=task_actions_dtos,
            task_ids=task_ids,
            task_stage_map=task_stage_map,
            assignees_dtos=assignees_dtos,
            task_ids_map=task_ids_map
        )

        return {
            "total_tasks": total_tasks,
            "tasks": tasks_list
        }

    def get_task_details_dict_from_dtos(
            self, task_fields_dtos: List[FieldDTO], task_ids_map,
            task_actions_dtos: List[ActionDTO], task_ids: List[int],
            task_stage_map, assignees_dtos: List[StageAssigneesDTO]):
        from collections import defaultdict
        tasks_fields_map = defaultdict(lambda: [])
        for task_fields_dto in task_fields_dtos:
            tasks_fields_map[task_fields_dto.task_id].append(
                task_fields_dto
            )
        assignees_dtos_dict = {}
        for assignees_dto in assignees_dtos:
            assignees_dtos_dict[
                assignees_dto.stage_id] = assignees_dto.assignees_details

        tasks_actions_map = defaultdict(lambda: [])
        for task_actions_dto in task_actions_dtos:
            tasks_actions_map[task_actions_dto.task_id].append(
                task_actions_dto
            )

        tasks_list = []
        for task_id in task_ids:
            fields_list = self._convert_fields_dtos_to_dict(
                field_dtos=tasks_fields_map[task_id]
            )
            actions_list = self._convert_action_dtos_to_dict(
                action_dtos=tasks_actions_map[task_id]
            )
            task_dict = self._get_task_details_dict(actions_list,
                                                    assignees_dtos_dict,
                                                    fields_list, task_id,
                                                    task_stage_map, display_id=task_ids_map[task_id])
            tasks_list.append(task_dict)
        return tasks_list

    def _get_task_details_dict(self, actions_list, assignees_dtos_dict,
                               fields_list, task_id, task_stage_map, display_id):
        task_dict = {
            "task_id": display_id,
            "task_overview_fields": fields_list,
            "stage_with_actions": {
                "stage_id": task_stage_map[task_id].db_stage_id,
                "stage_display_name": task_stage_map[task_id].display_name,
                "stage_color": task_stage_map[task_id].stage_color,
                "actions": actions_list
            }
        }
        try:
            assignees_details_dict = self._get_assignee_details_dict(
                assignees_dto=assignees_dtos_dict[task_stage_map[task_id].stage_id])
            task_dict['stage_with_actions'].update(assignees_details_dict)
        except KeyError:
            pass
        return task_dict

    @staticmethod
    def _get_assignee_details_dict(assignees_dto: AssigneesDTO):
        return {
            "assignee": {
                "assignee_id": assignees_dto.assignee_id,
                "name": assignees_dto.name,
                "profile_pic_url": assignees_dto.profile_pic_url
            }
        }

    @staticmethod
    def _convert_fields_dtos_to_dict(field_dtos: List[FieldDTO]):
        task_fields_list = []
        field_ids = []
        for field_dto in field_dtos:
            if field_dto.field_id not in field_ids:
                task_fields_list.append(
                    {
                        "field_id": field_dto.field_id,
                        "field_type": field_dto.field_type,
                        "field_display_name": field_dto.key,
                        "field_response": field_dto.value
                    }
                )
                field_ids.append(field_dto.field_id)
        return task_fields_list

    @staticmethod
    def _convert_action_dtos_to_dict(action_dtos: List[ActionDTO]):
        task_actions_list = []
        action_ids = []
        for action_dto in action_dtos:
            if action_dto.action_id not in action_ids:
                task_actions_list.append(
                    {
                        "action_id": action_dto.action_id,
                        "action_type": action_dto.action_type,
                        "button_text": action_dto.button_text,
                        "button_color": action_dto.button_color,
                        "transition_template_id": action_dto.transition_template_id
                    }
                )
                action_ids.append(action_dto.action_id)
        return task_actions_list


class GetColumnTasksListViewPresenterImplementation(
        HTTPResponseMixin, GetColumnTasksListViewPresenterInterface):
    def get_response_for_the_invalid_column_id(self):
        from ib_boards.constants.exception_messages import INVALID_COLUMN_ID
        response_dict = {
            "response": INVALID_COLUMN_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_COLUMN_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_stage_ids(self, error):
        pass

    def get_response_for_invalid_offset(self):
        from ib_boards.constants.exception_messages import INVALID_OFFSET_VALUE
        response_dict = {
            "response": INVALID_OFFSET_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_OFFSET_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_invalid_limit(self):
        from ib_boards.constants.exception_messages import INVALID_LIMIT_VALUE
        response_dict = {
            "response": INVALID_LIMIT_VALUE[0],
            "http_status_code": 400,
            "res_status": INVALID_LIMIT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    def get_response_for_user_have_no_access_for_column(self):
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_column_tasks_in_list_view(
            self, complete_tasks_details_dto: CompleteTasksDetailsDTO, all_fields: List[AllFieldsDTO]):
        presenter = GetColumnTasksPresenterImplementation()
        column_tasks_details_dict = presenter.get_column_tasks_details(
            complete_tasks_details_dto=complete_tasks_details_dto
        )
        all_fields_dict = self._get_all_fields_dict(
            all_fields=all_fields
        )
        column_tasks_details_dict.update(all_fields_dict)
        return self.prepare_200_success_response(column_tasks_details_dict)

    @staticmethod
    def _get_all_fields_dict(all_fields: List[AllFieldsDTO]):
        all_fields_dict = [
            {
                "field_id": all_fields_dto.field_id,
                "field_display_name": all_fields_dto.display_name,
                "display_order": all_fields_dto.display_order,
                "display_status": all_fields_dto.display_status
            }
            for all_fields_dto in all_fields
        ]
        return {
            "all_fields": all_fields_dict
        }


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def get_response_for_task_details(self,
                                      task_fields_dto: List[TaskFieldsDTO],
                                      task_actions_dto: List[TaskActionsDTO],
                                      task_ids: List[str]):
        pass

    def response_for_invalid_board_id(self) -> response.HttpResponse:
        response_object = {"response": INVALID_BOARD_ID[0],
                           "http_status_code": 404,
                           "res_status": INVALID_BOARD_ID[1]}
        return self.prepare_404_not_found_response(
            response_dict=response_object)

    def response_for_invalid_offset_value(self):
        response_object = {"response": INVALID_OFFSET_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_OFFSET_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def response_for_invalid_limit_value(self):
        response_object = {"response": INVALID_LIMIT_VALUE[0],
                           "http_status_code": 400,
                           "res_status": INVALID_LIMIT_VALUE[1]}
        return self.prepare_400_bad_request_response(response_object)

    def response_for_user_donot_have_access_for_board(self):
        response_object = {"response": USER_DONOT_HAVE_ACCESS[0],
                           "http_status_code": 403,
                           "res_status": USER_DONOT_HAVE_ACCESS[1]}
        return self.prepare_403_forbidden_response(response_object)

    def get_response_for_offset_exceeds_total_tasks(self):
        pass

    def get_response_for_column_details(
            self, column_details: List[ColumnCompleteDetails],
            task_fields_dtos: List[FieldDTO],
            task_actions_dtos: List[ActionDTO],
            column_tasks: List[ColumnTasksDTO],
            task_stage_dtos: List[TaskStageDTO],
            assignees_dtos: List[StageAssigneesDTO]) -> response.HttpResponse:

        task_ids_map = {}
        for column_task in column_tasks:
            task_ids_map[column_task.task_id] = column_task.task_display_id

        from collections import defaultdict
        column_stages_map = defaultdict(lambda: [])
        for column_stage in column_tasks:
            column_stages_map[column_stage.column_id].append(column_stage)

        columns_complete_details = []
        for column_dto in column_details:
            column_details_dict = self._get_column_complete_details(
                column_dto=column_dto,
                column_stages=column_stages_map[column_dto.column_id],
                task_fields_dtos=task_fields_dtos,
                task_actions_dtos=task_actions_dtos,
                task_stage_dtos=task_stage_dtos,
                assignees_dtos=assignees_dtos,
                task_ids_map=task_ids_map
            )
            columns_complete_details.append(column_details_dict)

        response_dict = {
            "total_columns_count": len(column_details),
            "columns": columns_complete_details
        }

        return self.prepare_200_success_response(response_dict)

    @staticmethod
    def _get_column_complete_details(
            column_dto: ColumnCompleteDetails,
            task_fields_dtos: List[FieldDTO],
            task_actions_dtos: List[ActionDTO],
            column_stages: List[ColumnTasksDTO],
            task_stage_dtos: List[TaskStageDTO],
            assignees_dtos: List[StageAssigneesDTO], task_ids_map):

        from collections import defaultdict
        column_tasks_map = defaultdict(lambda: [])
        for task_fields_dto in task_fields_dtos:
            column_tasks_map[
                task_fields_dto.stage_id + str(task_fields_dto.task_id)
                ].append(task_fields_dto)

        task_actions_map = defaultdict(lambda: [])
        for task_actions_dto in task_actions_dtos:
            task_actions_map[
                task_actions_dto.stage_id + str(task_actions_dto.task_id)
                ].append(task_actions_dto)

        task_ids = []
        for column_stage in column_stages:
            if column_stage.task_id not in task_ids:
                task_ids.append(column_stage.task_id)

        task_stage_map = {}
        for task_stage_dto in task_stage_dtos:
            task_stage_map[task_stage_dto.task_id] = task_stage_dto

        assignees_dtos_dict = {}
        for assignees_dto in assignees_dtos:
            assignees_dtos_dict[assignees_dto.stage_id] = assignees_dto

        task_fields_dtos_list = []
        task_actions_dtos_list = []
        assignees_dtos_list = []
        for column_stage in column_stages:
            task_fields_dtos_list += column_tasks_map[
                column_stage.stage_id + str(column_stage.task_id)]
            task_actions_dtos_list += task_actions_map[
                column_stage.stage_id + str(column_stage.task_id)]
            try:
                assignees_dtos_list.append(assignees_dtos_dict[column_stage.stage_id])
            except KeyError:
                pass

        presenter = GetColumnTasksPresenterImplementation()

        task_details_list = presenter.get_task_details_dict_from_dtos(
            task_fields_dtos=task_fields_dtos_list,
            task_actions_dtos=task_actions_dtos_list,
            task_ids=task_ids,
            task_stage_map=task_stage_map,
            assignees_dtos=assignees_dtos_list,
            task_ids_map=task_ids_map
        )

        return {
            "column_id": column_dto.column_id,
            "name": column_dto.name,
            "total_tasks": column_dto.total_tasks,
            "tasks": task_details_list
        }


class FieldsDisplayStatusPresenterImplementation(
        FieldsDisplayStatusPresenterInterface, HTTPResponseMixin):

    def get_response_for_the_invalid_column_id(self):
        from ib_boards.constants.exception_messages import INVALID_COLUMN_ID
        response_dict = {
            "response": INVALID_COLUMN_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_COLUMN_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_user_have_no_access_for_column(self):
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_field_not_belongs_to_column(self):
        from ib_boards.constants.exception_messages import \
            FIELD_NOT_BELONGS_TO_COLUMN
        response_dict = {
            "response": FIELD_NOT_BELONGS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": FIELD_NOT_BELONGS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )


class FieldsDisplayOrderPresenterImplementation(
        FieldsDisplayOrderPresenterInterface, HTTPResponseMixin):

    def get_response_for_the_invalid_column_id(self):
        from ib_boards.constants.exception_messages import INVALID_COLUMN_ID
        response_dict = {
            "response": INVALID_COLUMN_ID[0],
            "http_status_code": 404,
            "res_status": INVALID_COLUMN_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_response_for_user_have_no_access_for_column(self):
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        response_dict = {
            "response": USER_NOT_HAVE_ACCESS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_field_not_belongs_to_column(self, error):
        from ib_boards.constants.exception_messages import \
            FIELD_NOT_BELONGS_TO_COLUMN
        response_dict = {
            "response": FIELD_NOT_BELONGS_TO_COLUMN[0],
            "http_status_code": 403,
            "res_status": FIELD_NOT_BELONGS_TO_COLUMN[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def get_response_for_the_invalid_display_order(self):
        from ib_boards.constants.exception_messages import \
            INVALID_DISPLAY_ORDER
        response_dict = {
            "response": INVALID_DISPLAY_ORDER[0],
            "http_status_code": 400,
            "res_status": INVALID_DISPLAY_ORDER[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_field_order_in_column(
            self, all_fields: List[AllFieldsDTO]):
        response_dict = [
            {
                "field_id": all_fields_dto.field_id,
                "field_display_name": all_fields_dto.display_name,
                "display_order": all_fields_dto.display_order,
                "display_status": all_fields_dto.display_status
            }
            for all_fields_dto in all_fields
        ]
        return self.prepare_200_success_response(response_dict)


