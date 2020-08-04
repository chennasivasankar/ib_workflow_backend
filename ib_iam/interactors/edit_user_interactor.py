from typing import List

from ib_iam.exceptions.custom_exceptions import (
    UserIsNotAdmin, GivenNameIsEmpty, InvalidEmailAddress,
    RoleIdsAreInvalid, InvalidCompanyId, TeamIdsAreInvalid, UserDoesNotExist,
    NameShouldNotContainsNumbersSpecCharacters
)
from ib_iam.interactors.DTOs.common_dtos import \
    UserDetailsWithTeamRoleAndCompanyIdsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.edit_user_presenter_interface \
    import EditUserPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class EditUserInteractor(ValidationMixin):
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def edit_user_wrapper(
            self, admin_user_id: str, user_id: str,
            user_details_with_team_role_and_company_ids_dto \
                : UserDetailsWithTeamRoleAndCompanyIdsDTO,
            presenter: EditUserPresenterInterface
    ):
        try:
            self.edit_user(admin_user_id=admin_user_id, user_id=user_id,
                           user_details_with_team_role_and_company_ids_dto \
                               =user_details_with_team_role_and_company_ids_dto
                           )
            response = presenter.edit_user_success_response()
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        except UserDoesNotExist:
            response = presenter.raise_user_does_not_exist()
        except GivenNameIsEmpty:
            response = presenter.raise_invalid_name_exception()
        except InvalidEmailAddress:
            response = presenter.raise_invalid_email_exception()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter. \
                raise_name_should_not_contain_special_characters_exception()
        except RoleIdsAreInvalid:
            response = presenter.raise_role_ids_are_invalid()
        except InvalidCompanyId:
            response = presenter.raise_company_ids_is_invalid()
        except TeamIdsAreInvalid:
            response = presenter.raise_team_ids_are_invalid()
        return response

    def edit_user(
            self, admin_user_id: str, user_id: str,
            user_details_with_team_role_and_company_ids_dto):
        name = user_details_with_team_role_and_company_ids_dto.name
        team_ids = user_details_with_team_role_and_company_ids_dto.team_ids
        role_ids = user_details_with_team_role_and_company_ids_dto.role_ids
        company_id = user_details_with_team_role_and_company_ids_dto.company_id
        email = user_details_with_team_role_and_company_ids_dto.email

        self._check_and_throw_user_is_admin(user_id=admin_user_id)
        self._is_user_exist(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        self._validate_values(role_ids=role_ids, team_ids=team_ids,
                              company_id=company_id)
        self._update_user_profile_in_ib_users(
            user_id=user_id, email=email, name=name)
        self._update_user_roles_company_roles(
            user_id=user_id, company_id=company_id, role_ids=role_ids,
            team_ids=team_ids, name=name
        )

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.check_is_admin_user(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdmin()

    @staticmethod
    def _validate_email_and_throw_exception(email: str):
        import re
        email_valid_pattern = \
            r"(^[a-zA-Z]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]+$)"
        if not bool(re.match(email_valid_pattern, email)):
            raise InvalidEmailAddress()

    @staticmethod
    def _create_user_profile_dto(name, email, user_id):
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            name=name,
            email=email,
            user_id=user_id
        )
        return user_profile_dto

    def _validate_values(self, role_ids: List[str], team_ids: List[str],
                         company_id: str):
        self._validate_roles(role_ids=role_ids)
        self._validate_teams(team_ids=team_ids)
        self._validate_company(company_id=company_id)

    def _validate_roles(self, role_ids: List[str]):
        are_valid = self.storage.check_are_valid_role_ids(role_ids=role_ids)
        are_not_valid = not are_valid
        if are_not_valid:
            raise RoleIdsAreInvalid()

    def _validate_teams(self, team_ids: List[str]):
        are_valid = self.storage.check_are_valid_team_ids(team_ids=team_ids)
        are_not_valid = not are_valid
        if are_not_valid:
            raise TeamIdsAreInvalid()

    def _validate_company(self, company_id: str):
        is_valid = self.storage.check_is_exists_company_id(
            company_id=company_id
        )
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidCompanyId()

    def _is_user_exist(self, user_id: str):
        is_exist = self.storage.is_user_exist(user_id)
        is_not_exist = not is_exist
        if is_not_exist:
            raise UserDoesNotExist

    def _update_user_profile_in_ib_users(
            self, user_id: str, email: str, name: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = self._create_user_profile_dto(
            name=name, email=email, user_id=user_id)
        service_adapter.user_service.update_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)

    def _update_user_roles_company_roles(
            self, user_id: str, company_id: str,
            role_ids: List[str], team_ids: List[str], name: str):
        self._remove_existing_teams_roles_and_company(user_id)
        self._assaign_teams_roles_company_to_user(
            company_id, role_ids, team_ids, user_id, name
        )

    def _assaign_teams_roles_company_to_user(
            self, company_id: str, role_ids: List[str], team_ids: List[str],
            user_id: str, name: str):
        ids_of_role_objs = self.storage.get_role_objs_ids(role_ids)
        self.storage.add_roles_to_the_user(
            user_id=user_id, role_ids=ids_of_role_objs)
        self.storage.add_user_to_the_teams(user_id=user_id, team_ids=team_ids)
        self.storage.update_user_details(user_id=user_id,
                                         company_id=company_id, name=name)

    def _remove_existing_teams_roles_and_company(self, user_id: str):
        self.storage.remove_roles_for_user(user_id)
        self.storage.remove_teams_for_user(user_id)
