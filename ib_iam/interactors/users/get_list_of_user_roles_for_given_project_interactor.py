from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces. \
    user_presenter_interface import \
    GetListOfUserRolesForGivenProjectPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetListOfUserRolesForGivenProjectInteractor(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_list_of_user_roles_for_given_project_wrapper(
            self, project_id: str, user_id: str,
            presenter: GetListOfUserRolesForGivenProjectPresenterInterface
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        try:
            response = self._get_list_of_user_roles_for_given_project(
                project_id=project_id, presenter=presenter, user_id=user_id
            )
        except InvalidProjectId:
            response = presenter.response_for_invalid_project_id_exception()
        except UserIsNotAdmin:
            response = presenter.response_for_user_not_have_permission_exception()
        return response

    def _get_list_of_user_roles_for_given_project(
            self, project_id: str, user_id: str,
            presenter: GetListOfUserRolesForGivenProjectPresenterInterface
    ):
        basic_user_details_dtos, user_role_dtos = \
            self.get_list_of_user_roles_for_given_project(
                project_id=project_id, user_id=user_id
            )
        response = \
            presenter.get_response_for_get_users_with_roles(
                basic_user_details_dtos=basic_user_details_dtos,
                user_role_dtos=user_role_dtos
            )
        return response

    def get_list_of_user_roles_for_given_project(
            self, project_id: str, user_id: str
    ) -> tuple:
        self._validate_get_user_roles_details(
            project_id=project_id, user_id=user_id
        )
        basic_user_details_dtos = \
            self.user_storage.get_basic_user_dtos_for_given_project(
                project_id=project_id
            )
        user_ids = [
            basic_user_details_dto.user_id
            for basic_user_details_dto in basic_user_details_dtos
        ]
        user_role_dtos = self.user_storage.get_user_role_dtos_of_a_project(
            user_ids=user_ids, project_id=project_id
        )
        return basic_user_details_dtos, user_role_dtos

    def _validate_get_user_roles_details(self, project_id: str, user_id: str):
        self._validate_is_user_admin(user_id=user_id)
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        is_invalid_project_id = not self.user_storage.is_valid_project_id(
            project_id=project_id
        )
        if is_invalid_project_id:
            raise InvalidProjectId
