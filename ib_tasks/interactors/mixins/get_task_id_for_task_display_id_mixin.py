class GetTaskIdForTaskDisplayIdMixin:

    def get_task_id_for_task_display_id(self, task_display_id: str) -> int:
        is_valid_display_id = self.task_storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)
        is_invalid_display_id = not is_valid_display_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId

        if is_invalid_display_id:
            raise InvalidTaskDisplayId(task_display_id)

        task_id = self.task_storage.get_task_id_for_task_display_id(
            task_display_id=task_display_id)

        return task_id
