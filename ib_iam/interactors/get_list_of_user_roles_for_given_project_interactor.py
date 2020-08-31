from ib_iam.interactors.presenter_interfaces.get_list_of_user_roles_for_given_project_presenter_interface import \
    GetListOfUserRolesForGivenProjectPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetListOfUserRolesForGivenProjectInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_list_of_user_roles_for_given_project_wrapper(
            self, project_id: str,
            presenter: GetListOfUserRolesForGivenProjectPresenterInterface):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        try:
            response = self._get_list_of_user_roles_for_given_project(
                project_id=project_id,
                presenter=presenter)
        except InvalidProjectId:
            response = presenter.response_for_invalid_project_id()
        return response

    def _get_list_of_user_roles_for_given_project(
            self, project_id: str,
            presenter: GetListOfUserRolesForGivenProjectPresenterInterface):
        basic_user_details_dtos, user_role_dtos = \
            self.get_list_of_user_roles_for_given_project(
                project_id=project_id
            )
        response = \
            presenter.prepare_success_response_for_get_specific_project_details(
                basic_user_details_dtos=basic_user_details_dtos,
                user_role_dtos=user_role_dtos
            )
        return response

    def get_list_of_user_roles_for_given_project(self, project_id: str):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        is_invalid_project_id = not self.user_storage.is_valid_project_id(
            project_id=project_id)
        if is_invalid_project_id:
            raise InvalidProjectId

        basic_user_details_dtos = \
            self.user_storage.get_basic_user_dtos_for_given_project(
                project_id=project_id)
        user_ids = [
            basic_user_details_dto.user_id
            for basic_user_details_dto in basic_user_details_dtos
        ]
        user_role_dtos = self.user_storage.get_user_role_dtos_of_a_project(
            user_ids=user_ids, project_id=project_id
        )
        return basic_user_details_dtos, user_role_dtos
