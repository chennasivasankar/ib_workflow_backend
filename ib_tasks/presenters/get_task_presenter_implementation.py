from datetime import datetime
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.adapters.auth_service import \
    UsersNotExistsForGivenTeamsException, \
    TeamsNotExistForGivenProjectException, InvalidProjectIdsException
from ib_tasks.constants.constants import DATETIME_FORMAT
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException, \
    InvalidStageIdsForTask, InvalidTaskDisplayId
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import TaskCompleteDetailsDTO
from ib_tasks.interactors.stages_dtos import StageAssigneeWithTeamDetailsDTO, \
    AssigneeWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskGoFFieldDTO, TaskGoFDTO, TaskDetailsDTO
from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO


class GetTaskPresenterImplementation(GetTaskPresenterInterface,
                                     HTTPResponseMixin):

    def raise_invalid_user(self):
        from ib_tasks.constants.exception_messages import INVALID_USER
        response_message = INVALID_USER[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_USER[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_project_id(self, err: InvalidProjectIdsException):
        from ib_tasks.constants.exception_messages import INVALID_PROJECT_ID
        project_id = err.project_ids[0]
        response_message = INVALID_PROJECT_ID[0].format(project_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_PROJECT_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_teams_does_not_exists_for_project(
            self,
            err: TeamsNotExistForGivenProjectException
    ):
        from ib_tasks.constants.exception_messages import \
            TEAMS_NOT_EXISTS_FOR_PROJECT
        team_ids = err.team_ids
        response_message = TEAMS_NOT_EXISTS_FOR_PROJECT[0].format(team_ids)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": TEAMS_NOT_EXISTS_FOR_PROJECT[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_users_not_exist_for_given_teams(
            self,
            err: UsersNotExistsForGivenTeamsException
    ):
        from ib_tasks.constants.exception_messages import \
            USERS_NOT_EXISTS_FOR_TEAMS
        user_ids = err.user_ids
        response_message = USERS_NOT_EXISTS_FOR_TEAMS[0].format(user_ids)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": USERS_NOT_EXISTS_FOR_TEAMS[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_searchable_records_found(self):
        from ib_tasks.constants.exception_messages import \
            SEARCHABLE_RECORDS_NOT_FOUND
        response_message = SEARCHABLE_RECORDS_NOT_FOUND[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": SEARCHABLE_RECORDS_NOT_FOUND[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_user_permission_denied(self):
        from ib_tasks.constants.exception_messages import \
            USER_PERMISSION_DENIED
        response_message = USER_PERMISSION_DENIED[0]
        data = {
            "response": response_message,
            "http_status_code": 403,
            "res_status": USER_PERMISSION_DENIED[1]
        }
        response_object = self.prepare_403_forbidden_response(
            response_dict=data
        )
        return response_object

    def raise_exception_for_invalid_task_id(self, err: InvalidTaskIdException):
        from ib_tasks.constants.exception_messages import INVALID_TASK_DB_ID
        response_message = INVALID_TASK_DB_ID[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_DB_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_stage_ids_for_task(self, err: InvalidStageIdsForTask):
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGES_FOR_TASK
        response_message = INVALID_STAGES_FOR_TASK[0]
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_STAGES_FOR_TASK[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def raise_invalid_task_display_id(self, err: InvalidTaskDisplayId):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        task_id = err.task_display_id
        response_message = INVALID_TASK_DISPLAY_ID[0].format(task_id)
        data = {
            "response": response_message,
            "http_status_code": 404,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        response_object = self.prepare_404_not_found_response(
            response_dict=data
        )
        return response_object

    def get_task_response(
            self, task_complete_details_dto: TaskCompleteDetailsDTO
    ):
        task_details_dto = task_complete_details_dto.task_details_dto
        task_base_details_dto = task_details_dto.task_base_details_dto
        project_info = self._get_project_details(task_details_dto)
        gofs = self._get_task_gofs(task_details_dto)
        task_stage_complete_details_dtos = \
            task_complete_details_dto.stages_and_actions_details_dtos
        stage_assignee_with_team_details_dtos = \
            task_complete_details_dto.stage_assignee_with_team_details_dtos
        stages_with_actions = self._get_task_stages_with_actions_details(
            task_stage_complete_details_dtos,
            stage_assignee_with_team_details_dtos
        )
        start_date = self._convert_datetime_object_to_string(
            task_base_details_dto.start_date
        )
        due_date = self._convert_datetime_object_to_string(
            task_base_details_dto.due_date
        )
        task_details_dict = {
            "task_id": task_base_details_dto.task_display_id,
            "project_info": project_info,
            "template_id": task_base_details_dto.template_id,
            "title": task_base_details_dto.title,
            "description": task_base_details_dto.description,
            "start_date": start_date,
            "due_date": due_date,
            "priority": task_base_details_dto.priority,
            "gofs": gofs,
            "stages_with_actions": stages_with_actions
        }
        response_object = self.prepare_200_success_response(
            response_dict=task_details_dict
        )
        return response_object

    @staticmethod
    def _get_project_details(
            task_details_dto: TaskDetailsDTO
    ) -> Dict:
        project_details_dto = task_details_dto.project_details_dto
        project_info = {
            "project_id": project_details_dto.project_id,
            "project_name": project_details_dto.name,
            "project_logo_url": project_details_dto.logo_url
        }
        return project_info

    @staticmethod
    def _convert_datetime_object_to_string(
            datetime_obj: datetime
    ):
        datetime_in_string_format = datetime_obj.strftime(DATETIME_FORMAT)
        return datetime_in_string_format

    def _get_task_stages_with_actions_details(
            self,
            task_stage_complete_details_dtos: List[StageAndActionsDetailsDTO],
            stage_assignee_with_team_details_dtos: List[
                StageAssigneeWithTeamDetailsDTO]
    ):
        stages_with_actions = []
        for task_stage_complete_details_dto in \
                task_stage_complete_details_dtos:
            stage_details_dict = self._prepare_stage_details_dict(
                task_stage_complete_details_dto,
                stage_assignee_with_team_details_dtos
            )
            stages_with_actions.append(stage_details_dict)
        return stages_with_actions

    def _prepare_stage_details_dict(
            self, task_stage_complete_details_dto: StageAndActionsDetailsDTO,
            stage_assignee_with_team_details_dtos: List[
                StageAssigneeWithTeamDetailsDTO]
    ):
        actions_dtos = task_stage_complete_details_dto.actions_dtos
        actions = self._get_action_details(actions_dtos)
        task_stage_id = self._get_task_stage_id(
            task_stage_complete_details_dto,
            stage_assignee_with_team_details_dtos
        )
        assignee_details = self._get_assignee_with_team_details_dto(
            task_stage_complete_details_dto,
            stage_assignee_with_team_details_dtos
        )
        stage_details_dict = {
            "stage_id": task_stage_complete_details_dto.db_stage_id,
            "stage_display_name": task_stage_complete_details_dto.name,
            "stage_color": task_stage_complete_details_dto.color,
            "task_stage_id": task_stage_id,
            "assignee": assignee_details,
            "actions": actions
        }
        return stage_details_dict

    @staticmethod
    def _get_task_stage_id(
            task_stage_complete_details_dto,
            stage_assignee_with_team_details_dtos
    ) -> int:
        db_stage_id = task_stage_complete_details_dto.db_stage_id
        for stage_assignee_with_team_details_dto in \
                stage_assignee_with_team_details_dtos:
            stage_id = stage_assignee_with_team_details_dto.stage_id
            if db_stage_id == stage_id:
                task_stage_id = \
                    stage_assignee_with_team_details_dto.task_stage_id
                return task_stage_id

    def _get_assignee_with_team_details_dto(
            self, task_stage_complete_details_dto: StageAndActionsDetailsDTO,
            stage_assignee_with_team_details_dtos: List[
                StageAssigneeWithTeamDetailsDTO]
    ):
        db_stage_id = task_stage_complete_details_dto.db_stage_id
        for stage_assignee_with_team_details_dto in \
                stage_assignee_with_team_details_dtos:
            stage_id = stage_assignee_with_team_details_dto.stage_id
            if db_stage_id == stage_id:
                assignee_with_team_details_dto = \
                    stage_assignee_with_team_details_dto.assignee_details_dto
                if assignee_with_team_details_dto:
                    assignee_details_dict = \
                        self._get_assignee_details_dict(
                            assignee_with_team_details_dto)
                else:
                    assignee_details_dict = None
                return assignee_details_dict

    @staticmethod
    def _get_assignee_details_dict(
            assignee_with_team_details_dto: AssigneeWithTeamDetailsDTO
    ) -> Dict:
        team_info_dto = assignee_with_team_details_dto.team_info_dto
        team_info = {
            "team_id": team_info_dto.team_id,
            "team_name": team_info_dto.team_name
        }
        assignee_with_team_details_dict = {
            "assignee_id": assignee_with_team_details_dto.assignee_id,
            "name": assignee_with_team_details_dto.name,
            "profile_pic_url": assignee_with_team_details_dto.profile_pic_url,
            "team_info": team_info
        }
        return assignee_with_team_details_dict

    def _get_action_details(self, actions_dtos: List[StageActionDetailsDTO]):
        actions = []
        for actions_dto in actions_dtos:
            action_dict = self._prepare_action_dict(actions_dto)
            actions.append(action_dict)
        return actions

    @staticmethod
    def _prepare_action_dict(actions_dto: StageActionDetailsDTO):
        action_dict = {
            "action_id": actions_dto.action_id,
            "action_type": actions_dto.action_type,
            "button_text": actions_dto.button_text,
            "button_color": actions_dto.button_color,
            "transition_template_id": actions_dto.transition_template_id
        }
        return action_dict

    def _get_task_gofs(
            self, task_details_dto: TaskDetailsDTO
    ) -> List[Dict]:

        task_gof_dtos = task_details_dto.task_gof_dtos
        task_gof_field_dtos = task_details_dto.task_gof_field_dtos
        gofs = []
        for task_gof_dto in task_gof_dtos:
            task_gof_id = task_gof_dto.task_gof_id
            gof_fields = self._get_gof_fields(task_gof_id, task_gof_field_dtos)
            gof_dict = self._prepare_gof_dict(task_gof_dto, gof_fields)
            gofs.append(gof_dict)
        return gofs

    @staticmethod
    def _prepare_gof_dict(task_gof_dto: TaskGoFDTO, gof_fields: List[Dict]):
        gof_dict = {
            "gof_id": task_gof_dto.gof_id,
            "same_gof_order": task_gof_dto.same_gof_order,
            "gof_fields": gof_fields
        }
        return gof_dict

    def _get_gof_fields(
            self, task_gof_id: int, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        gof_fields = []
        for task_gof_field_dto in task_gof_field_dtos:
            if task_gof_id == task_gof_field_dto.task_gof_id:
                field_dict = self._prepare_field_dict(task_gof_field_dto)
                gof_fields.append(field_dict)
        return gof_fields

    @staticmethod
    def _prepare_field_dict(task_gof_field_dto: TaskGoFFieldDTO):
        field_dict = {
            "field_id": task_gof_field_dto.field_id,
            "field_response": task_gof_field_dto.field_response
        }
        return field_dict

    def response_for_invalid_task_id(self):
        pass

    def response_for_user_is_not_assignee_for_task(self):
        pass

    def get_response_for_get_task_due_details(self, task_dtos):
        pass
