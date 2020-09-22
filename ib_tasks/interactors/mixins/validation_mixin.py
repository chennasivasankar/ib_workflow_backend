from typing import List, Optional

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException, \
    UserIsNotInProjectException, UserIsNotInProjectsException
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.action_custom_exceptions import \
    InvalidActionException
from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException


class ValidationMixin:
    def validate_task_id(self, task_id: int) -> \
            Optional[InvalidTaskIdException]:
        is_task_exists = self.task_storage. \
            check_is_task_exists(task_id=task_id)
        is_task_does_not_exists = not is_task_exists

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        if is_task_does_not_exists:
            raise InvalidTaskIdException(task_id=task_id)
        return

    def validate_action_id(self, action_id: int) -> \
            Optional[InvalidActionException]:
        valid_action = self.action_storage.validate_action(action_id=action_id)
        is_invalid_action = not valid_action

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        if is_invalid_action:
            raise InvalidActionException(action_id=action_id)
        return

    def check_is_valid_stage_id(self, stage_id: int) -> bool:
        is_valid_stage = \
            self.stage_storage.check_is_stage_exists(stage_id=stage_id)
        return is_valid_stage

    def validate_given_project_ids(self, project_ids: List[str]):
        """
        @param project_ids:
        @type project_ids:
        @raise: InvalidProjectIdsException
        @rtype:
        """
        adapter = self.get_service_adapter()
        valid_project_ids = adapter.auth_service.validate_project_ids(
            project_ids)
        invalid_project_ids = [project_id for project_id in project_ids
                               if project_id not in valid_project_ids]
        if invalid_project_ids:
            raise InvalidProjectIdsException(invalid_project_ids)

    def validate_if_user_is_in_projects(self, user_id: str, project_ids):

        adapter = self.get_service_adapter()
        user_project_status_dtos = adapter.auth_service \
            .validate_if_user_is_in_projects(
            user_id=user_id, project_ids=project_ids
        )
        user_not_in_projects = [
            user_project_status_dto.project_id
            for user_project_status_dto in user_project_status_dtos
            if not user_project_status_dto.is_exists
        ]
        if user_not_in_projects:
            raise UserIsNotInProjectsException(project_ids=project_ids)

    def validate_if_user_is_in_project(self, user_id: str,
                                       project_id: str):
        """
        @param user_id:
        @type user_id:
        @param project_id:
        @type project_id:
        @raise: UserIsNotInProjectException
        @rtype:
        """
        adapter = self.get_service_adapter()
        try:
            is_in_project = adapter.auth_service.validate_if_user_is_in_project(
                user_id=user_id, project_id=project_id)
        except InvalidProjectId:
            raise InvalidProjectIdsException([project_id])

        if not is_in_project:
            raise UserIsNotInProjectException

    @staticmethod
    def get_service_adapter():
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        return service_adapter

    def validate_filter_id(self, filter_id: int):
        self.filter_storage.validate_filter_id(
            filter_id=filter_id
        )

    def validate_user_with_filter_id(self, user_id: str, filter_id: int):
        self.filter_storage.validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )
