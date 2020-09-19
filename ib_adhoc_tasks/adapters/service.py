from typing import List


class Service:

    @staticmethod
    def get_user_role_ids_based_on_project(
            user_id: str, project_id: str
    ) -> List[str]:
        pass

    @staticmethod
    def get_stage_ids_based_on_user_roles(
            user_role_ids: List[str]
    ) -> List[str]:
        pass
