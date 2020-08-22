from typing import List, Optional

from ib_boards.adapters.iam_service import UserIsNotInProject, \
    InvalidProjectIds


class ValidationMixin:
    def validate_task_id(self, task_id: int):
        is_task_exists = self.task_storage. \
            check_is_task_exists(task_id=task_id)
        is_task_does_not_exists = not is_task_exists

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        if is_task_does_not_exists:
            raise InvalidTaskIdException(task_id=task_id)

    def validate_action_id(self, action_id: int):
        valid_action = self.action_storage.validate_action(action_id=action_id)
        is_invalid_action = not valid_action

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        if is_invalid_action:
            raise InvalidActionException(action_id=action_id)

    def check_is_valid_stage_id(self, stage_id: int) -> bool:
        is_valid_stage = \
            self.stage_storage.check_is_stage_exists(stage_id=stage_id)
        return is_valid_stage

    def validate_given_project_ids(self, project_ids: List[str]) -> \
            Optional[InvalidProjectIds]:
        raise NotImplementedError

    def validate_if_user_is_in_project(self, user_id: str,
                                       project_id: str) -> \
            Optional[UserIsNotInProject]:
        raise NotImplementedError
