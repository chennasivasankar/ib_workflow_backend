from typing import List

from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.presenter_interfaces.add_specific_project_details_presenter_interface import \
    AddSpecificProjectDetailsPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AddSpecificProjectDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_specific_project_details_wrapper(
            self, project_id: str,
            user_id_with_role_ids_dtos: List[UserIdWithRoleIdsDTO],
            presenter: AddSpecificProjectDetailsPresenterInterface
    ):
        response = self._add_specific_project_details_response(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id, presenter=presenter
        )
        return response

    def _add_specific_project_details_response(
            self, project_id: str,
            user_id_with_role_ids_dtos: List[UserIdWithRoleIdsDTO],
            presenter: AddSpecificProjectDetailsPresenterInterface
    ):
        self.add_specific_project_details(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )
        response = presenter. \
            prepare_success_response_for_add_specific_project_details()
        return response

    def add_specific_project_details(
            self, project_id: str,
            user_id_with_role_ids_dtos: List[UserIdWithRoleIdsDTO]
    ):
        self.user_storage.add_project_specific_details(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )
        return
