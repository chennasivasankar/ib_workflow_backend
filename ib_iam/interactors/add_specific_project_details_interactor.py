from typing import List

from ib_iam.exceptions.custom_exceptions import InvalidUserIdsForProject, \
    InvalidRoleIdsForProject, InvalidProjectId
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
        try:
            response = self._add_specific_project_details_response(
                user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
                project_id=project_id, presenter=presenter
            )
        except InvalidProjectId:
            response = presenter.response_for_invalid_project_id()
        except InvalidUserIdsForProject as err:
            response = presenter.response_for_invalid_user_ids_for_project(err)
        except InvalidRoleIdsForProject as err:
            response = presenter.response_for_invalid_role_ids_for_project(err)
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
        user_ids = [
            user_id_with_role_ids_dto.user_id
            for user_id_with_role_ids_dto in user_id_with_role_ids_dtos
        ]
        role_ids = []
        for user_id_with_role_ids_dto in user_id_with_role_ids_dtos:
            role_ids.extend(user_id_with_role_ids_dto.role_ids)

        self.user_storage.validate_project_id(project_id=project_id)
        self.user_storage.validate_users_for_project(
            user_ids=user_ids, project_id=project_id
        )
        self.user_storage.validate_role_ids_for_project(
            role_ids=role_ids, project_id=project_id
        )
        self.user_storage.assign_user_roles_for_given_project(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )
        return
