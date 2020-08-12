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

    def validate_stage_id(self, stage_id: int):
        is_valid_stage = \
            self.stage_storage.check_is_stage_exists(stage_id=stage_id)

        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageId
        is_invalid_stage = not is_valid_stage
        if is_invalid_stage:
            raise InvalidStageId(stage_id)
