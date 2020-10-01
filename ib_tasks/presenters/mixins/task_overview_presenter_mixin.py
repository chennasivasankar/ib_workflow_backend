from typing import List, Optional, Dict

from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO


class TaskOverviewDetailsPresenterMixin:

    def _prepare_task_overview_details_dict(
            self, all_tasks_overview_dto: AllTasksOverviewDetailsDTO
    ):
        task_stages_has_no_actions = \
            not all_tasks_overview_dto.task_with_complete_stage_details_dtos
        if task_stages_has_no_actions:
            return None
        complete_task_stage_details_dto = \
            all_tasks_overview_dto.task_with_complete_stage_details_dtos[0]
        task_fields_action_details_dtos = \
            all_tasks_overview_dto.task_fields_and_action_details_dtos
        task_stage_details_dto = \
            complete_task_stage_details_dto.task_with_stage_details_dto
        task_overview_fields_details, actions_details = \
            self.task_fields_and_actions_details(
                task_stage_details_dto.task_id, task_fields_action_details_dtos
            )
        assignee = self._get_assignee_details(
            complete_task_stage_details_dto.stage_assignee_dto)
        task_base_details = all_tasks_overview_dto.task_base_details_dtos[0]
        start_date = task_base_details.start_date
        due_date = task_base_details.due_date
        if start_date is not None:
            start_date = str(start_date)
        if due_date is not None:
            due_date = str(due_date)
        task_overview_details_dict = {
            "task_id": task_stage_details_dto.task_display_id,
            "template_id": task_base_details.template_id,
            "title": task_base_details.title,
            "start_date": start_date,
            "due_date": due_date,
            "priority": task_base_details.priority,
            "task_overview_fields": task_overview_fields_details,
            "stage_with_actions": {
                "stage_id":
                    task_stage_details_dto.db_stage_id,
                "stage_display_name":
                    task_stage_details_dto.stage_display_name,
                "stage_color":
                    task_stage_details_dto.stage_color,
                "assignee": assignee,
                "actions": actions_details
            }
        }
        return task_overview_details_dict

    def task_fields_and_actions_details(
            self, given_task_id: int,
            task_fields_and_action_details_dtos: List[
                GetTaskStageCompleteDetailsDTO]):
        for each_task_fields_and_action_details_dto in \
                task_fields_and_action_details_dtos:
            if given_task_id == \
                    each_task_fields_and_action_details_dto.task_id:
                task_overview_fields_details = \
                    self._get_task_overview_fields_details(
                        each_task_fields_and_action_details_dto)
                action_details = self._get_actions_details_of_task_stage(
                    each_task_fields_and_action_details_dto)
                return task_overview_fields_details, action_details
        return [], []

    @staticmethod
    def _get_task_overview_fields_details(
            each_task_fields_and_action_details_dto):
        field_dtos = each_task_fields_and_action_details_dto.field_dtos
        field_dtos.sort(key=lambda x: [x.order])
        task_overview_fields_details = [
            {
                "field_type": each_field_dto.field_type,
                "field_display_name": each_field_dto.key,
                "field_response": each_field_dto.value
            } for each_field_dto in field_dtos
        ]
        return task_overview_fields_details

    @staticmethod
    def _get_actions_details_of_task_stage(
            each_task_fields_and_action_details_dto):
        action_details = [{
            "action_id": each_action_dto.action_id,
            "button_text": each_action_dto.button_text,
            "button_color": each_action_dto.button_color,
            "action_type": each_action_dto.action_type,
            "transition_template_id": each_action_dto.transition_template_id
        } for each_action_dto in
            each_task_fields_and_action_details_dto.action_dtos]
        return action_details

    @staticmethod
    def _get_assignee_details(
            stage_assignee_dto: List[TaskStageAssigneeTeamDetailsDTO]
    ) -> Optional[Dict]:
        if stage_assignee_dto:
            assignee_details_dto = stage_assignee_dto[0].assignee_details
        else:
            return None
        if assignee_details_dto:
            team_details_dto = stage_assignee_dto[0].team_details
            assignee_details = {
                "assignee_id": assignee_details_dto.assignee_id,
                "name": assignee_details_dto.name,
                "profile_pic_url": assignee_details_dto.profile_pic_url,
                "team_info": {
                    "team_id": team_details_dto.team_id,
                    "team_name": team_details_dto.name
                }
            }
            return assignee_details
