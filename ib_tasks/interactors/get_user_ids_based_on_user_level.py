"""
Created on: 29/09/20
Author: Pavankumar Pamuru

"""
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin


class GetUserIdsBasedOnUserLevel(ValidationMixin):
    def __init__(self):
        pass

    def get_user_ids_based_on_user_level(self, project_id: str, user_id: str):
        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()

        is_user_in_least_level = service_adapter.auth_service.check_user_in_least_level(
            project_id=project_id,
            user_id=user_id
        )
        if is_user_in_least_level:
            return [user_id]

        user_ids = service_adapter.auth_service.get_user_ids_based_on_user_level(
            project_id=project_id,
            user_id=user_id
        )
        return user_ids
