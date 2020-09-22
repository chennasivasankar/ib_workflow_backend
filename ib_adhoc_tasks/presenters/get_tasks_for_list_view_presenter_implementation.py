from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO, \
    TaskBaseDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    TaskStageAssigneeDetailsDTO, FieldDetailsDTO, StageActionDetailsDTO, \
    AssigneeDetailsDTO, TeamDetailsDTO
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_tasks_for_list_view_presenter_interface import \
    GetTasksForListViewPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO


class GetTasksForListViewPresenterImplementation(
        GetTasksForListViewPresenterInterface, HTTPResponseMixin):

    def raise_invalid_project_id(self):
        from ib_adhoc_tasks.constants.exception_messages import \
            INVALID_PROJECT_ID
        response_message = INVALID_PROJECT_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def get_task_details_group_by_info_response(
            self,
            group_details_dtos: List[GroupDetailsDTO],
            task_details_dto: TasksCompleteDetailsDTO
    ):
        groups = []
        for group_details_dto in group_details_dtos:
            tasks = self._get_tasks_details_for_group(
                group_details_dto, task_details_dto)
            each_group_details = {
                "group_by_value": group_details_dto.group_by_value,
                "group_by_display_name": group_details_dto.group_by_display_name,
                "total_tasks": group_details_dto.total_tasks,
                "tasks": tasks
            }
            groups.append(each_group_details)

        total_groups = len(group_details_dtos)
        all_group_details = {
            "total_groups": total_groups,
            "groups": groups
        }
        response_object = self.prepare_200_success_response(
            response_dict=all_group_details
        )
        return response_object

    def _get_tasks_details_for_group(
            self, group_details_dto: GroupDetailsDTO,
            task_details_dto: TasksCompleteDetailsDTO
    ):
        task_ids = group_details_dto.task_ids
        task_base_details_dtos = task_details_dto.task_base_details_dtos
        task_stage_details_dtos = task_details_dto.task_stage_details_dtos
        task_stage_assignee_dtos = task_details_dto.task_stage_assignee_dtos

        tasks = []
        for task_id in task_ids:
            task_base_details_dto = self._get_task_base_details_dto(
                task_id, task_base_details_dtos
            )
            task_stage_details_dto = self._get_task_stage_details_dto(
                task_id, task_stage_details_dtos
            )
            stage_id = task_stage_details_dto.stage_id
            task_stage_assignee_dto = self._get_task_stage_assignee_dto(
                task_id, stage_id, task_stage_assignee_dtos
            )
            task_dict = self._get_task_details(
                task_base_details_dto, task_stage_details_dto,
                task_stage_assignee_dto
            )
            tasks.append(task_dict)
        return tasks

    @staticmethod
    def _get_task_base_details_dto(
            task_id: int,
            task_base_details_dtos: List[TaskBaseDetailsDTO]
    ) -> TaskBaseDetailsDTO:

        for task_base_details_dto in task_base_details_dtos:
            if task_id == task_base_details_dto.task_id:
                return task_base_details_dto

    @staticmethod
    def _get_task_stage_details_dto(
            task_id: int,
            task_stage_details_dtos: List[GetTaskStageCompleteDetailsDTO]
    ) -> GetTaskStageCompleteDetailsDTO:

        for task_stage_details_dto in task_stage_details_dtos:
            if task_id == task_stage_details_dto.task_id:
                return task_stage_details_dto

    @staticmethod
    def _get_task_stage_assignee_dto(
            task_id: int, stage_id: str,
            task_stage_assignee_dtos: List[TaskStageAssigneeDetailsDTO]
    ):
        for task_stage_assignee_dto in task_stage_assignee_dtos:
            assignee_task_id = task_stage_assignee_dto.task_id
            assignee_stage_id = task_stage_assignee_dto.stage_id
            is_assignee_for_stage = task_id == assignee_task_id and \
                        stage_id == assignee_stage_id
            if is_assignee_for_stage:
                return task_stage_assignee_dto

    def _get_task_details(
            self, task_base_details_dto: TaskBaseDetailsDTO,
            task_stage_details_dto: GetTaskStageCompleteDetailsDTO,
            task_stage_assignee_dto: TaskStageAssigneeDetailsDTO
    ) -> Dict:
        field_dtos = task_stage_details_dto.field_dtos
        task_overview_fields = self._get_task_overview_fields(field_dtos)
        stage_with_actions = self._get_stages_with_actions(
            task_stage_details_dto, task_stage_assignee_dto
        )
        task_dict = {
            "task_id": task_base_details_dto.task_display_id,
            "title": task_base_details_dto.title,
            "description": task_base_details_dto.description,
            "start_date": task_base_details_dto.start_date,
            "due_date": task_base_details_dto.due_date,
            "priority": task_base_details_dto.priority,
            "task_overview_fields": task_overview_fields,
            "stage_with_actions": stage_with_actions
        }
        return task_dict

    def _get_stages_with_actions(
            self, task_stage_details_dto: GetTaskStageCompleteDetailsDTO,
            task_stage_assignee_dto: TaskStageAssigneeDetailsDTO
    ):
        action_dtos = task_stage_details_dto.action_dtos
        assignee_dto = task_stage_assignee_dto.assignee_details
        assignee = None
        if assignee_dto:
            team_dto = task_stage_assignee_dto.team_details
            assignee = self._get_assignee_with_team_details(assignee_dto,
                                                            team_dto)
        actions = self._get_stage_actions(action_dtos)
        stage_with_actions = {
            "stage_id": task_stage_details_dto.stage_id,
            "stage_display_name": task_stage_details_dto.display_name,
            "stage_color": task_stage_details_dto.stage_color,
            "assignee": assignee,
            "actions": actions
        }
        return stage_with_actions

    @staticmethod
    def _get_assignee_with_team_details(
            assignee_dto: AssigneeDetailsDTO, team_dto: TeamDetailsDTO
    ):
        team_info = {
            "team_id": team_dto.team_id,
            "team_name": team_dto.name
        }
        assignee_details = {
            "assignee_id": assignee_dto.assignee_id,
            "name": assignee_dto.name,
            "profile_pic_url": assignee_dto.profile_pic_url,
            "team_info": team_info
        }
        return assignee_details

    @staticmethod
    def _get_stage_actions(
            action_dtos: List[StageActionDetailsDTO]
    ) -> List[Dict]:
        actions = [
            {
                "action_id": action_dto.action_id,
                "action_type": action_dto.action_type,
                "button_text": action_dto.button_text,
                "button_color": action_dto.button_color
            }
            for action_dto in action_dtos
        ]
        return actions

    @staticmethod
    def _get_task_overview_fields(
            field_dtos: List[FieldDetailsDTO]
    ) -> List[Dict]:
        task_overview_fields = [
            {
                "field_type": field_dto.field_type,
                "field_display_name": field_dto.key,
                "field_response": field_dto.value,
                "field_id": field_dto.field_id
            }
            for field_dto in field_dtos
        ]
        return task_overview_fields




