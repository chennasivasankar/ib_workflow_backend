from typing import List


class IAMService:

    def is_project_exists(self, project_id: str) -> bool:
        pass

    @staticmethod
    def get_user_role_ids_based_on_project(
            user_id: str, project_id: str
    ) -> List[str]:
        pass
