import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import BasicUserDetailsDTO, \
    UserRoleDTO
from ib_iam.interactors.presenter_interfaces.dtos import UserOptionsDetailsDTO

from ib_iam.interactors.presenter_interfaces.dtos import \
    ListOfCompleteUsersWithRolesDTO


class AssignUserRolesForGivenProjectBulkPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_assign_user_roles_for_given_project(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_for_project(self, err):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_for_project(self, err):
        pass

    @abc.abstractmethod
    def response_for_invalid_project_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass


class GetListOfUserRolesForGivenProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_users_with_roles(
            self, basic_user_details_dtos: List[BasicUserDetailsDTO],
            user_role_dtos: List[UserRoleDTO]
    ):
        pass

    @abc.abstractmethod
    def response_for_invalid_project_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_not_have_permission_exception(self):
        pass


class GetUserOptionsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def get_user_options_details_response(
            self, configuration_details_dto: UserOptionsDetailsDTO
    ):
        pass


class GetUsersListPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abc.abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: ListOfCompleteUsersWithRolesDTO):
        pass

    @abc.abstractmethod
    def raise_invalid_user(self):
        pass


class EditUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def edit_user_success_response(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(self):
        pass

    @abc.abstractmethod
    def raise_role_ids_are_invalid(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_does_not_exist(self):
        pass


class AddUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_name_length_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_email_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_account_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def response_for_name_contains_special_character_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_company_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_add_user_response(self):
        pass


class DeleteUserPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_delete_user_response(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_is_not_found_exception(self):
        pass

    @abc.abstractmethod
    def raise_user_does_not_have_delete_permission_exception(self):
        pass
