from typing import List, Optional

from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidTaskTemplateId


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def validate_task_template_id(self, task_template_id: str) -> \
            Optional[InvalidTaskTemplateId]:
        pass

    @staticmethod
    def get_stage_ids_based_on_user_roles(
            user_role_ids: List[str]
    ) -> List[str]:
        pass
