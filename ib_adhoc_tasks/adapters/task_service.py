from typing import List


class TaskService:

    def is_template_exists(self, template_id: str) -> bool:
        pass

    @staticmethod
    def get_stage_ids_based_on_user_roles(
            user_role_ids: List[str]
    ) -> List[str]:
        pass
