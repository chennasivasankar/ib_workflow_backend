from typing import Optional


class InvalidTaskTemplateId(Exception):
    pass


class InvalidGroupById(Exception):
    pass


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_stage_ids_having_actions(self):
        pass

    def validate_task_template_id(self, task_template_id: str) -> \
            Optional[InvalidTaskTemplateId]:
        valid_task_template_ids = self.interface.validate_task_template_ids(
            task_template_ids=[task_template_id]
        )
        is_invalid_task_template_id = not valid_task_template_ids
        if is_invalid_task_template_id:
            raise InvalidTaskTemplateId
        return
