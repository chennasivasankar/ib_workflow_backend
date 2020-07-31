from typing import List

from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, \
    GivenNameIsEmpty, \
    InvalidEmailAddress, \
    UserAccountAlreadyExistWithThisEmail, \
    NameShouldNotContainsNumbersSpecCharacters, \
    RoleIdsAreInvalid, InvalidCompanyId, \
    TeamIdsAreInvalid
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
    import AddUserPresenterInterface
from ib_iam.interactors.storage_interfaces.add_new_user_storage_interface \
    import AddNewUserStorageInterface


class AddNewUserInteractor(ValidationMixin):
    def __init__(self, storage: AddNewUserStorageInterface):
        self.storage = storage

    def add_new_user_wrapper(
            self, user_id: str, name: str, email: str,
            teams: List[str], roles: List[str], company_id: str,
            presenter: AddUserPresenterInterface):
        try:
            self.add_new_user(user_id=user_id, name=name, email=email,
                              roles=roles, teams=teams, company_id=company_id)
            response = presenter.user_created_response()
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        except GivenNameIsEmpty:
            response = presenter.raise_invalid_name_exception()
        except InvalidEmailAddress:
            response = presenter.raise_invalid_email_exception()
        except UserAccountAlreadyExistWithThisEmail:
            response = presenter. \
                raise_user_account_already_exist_with_this_email_exception()
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

    def add_new_user(self, user_id: str, name: str, email: str,
                     roles: List[str], teams: List[str], company_id: str):
        self._check_and_throw_user_is_admin(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        self._validate_values(roles, teams, company_id)
        new_user_id = self._create_user_in_ib_users(email, name)
        role_ids = self.storage.get_role_objs_ids(roles)
        self.storage.add_new_user(
            user_id=new_user_id, is_admin=False, company_id=company_id,
            role_ids=role_ids, team_ids=teams, name=name
        )

    def _create_user_in_ib_users(self, email, name):
        new_user_id = self._create_user_account_with_email(email=email)
        self._create_user_profile(user_id=new_user_id, email=email, name=name)
        return new_user_id

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
    def _create_user_account_with_email(email: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service. \
            create_user_account_with_email(email=email)
        return user_id

    def _create_user_profile(self, user_id: str, email: str, name: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_profile_dto = self._create_user_profile_dto(
            name=name, email=email, user_id=user_id)
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)

    @staticmethod
    def _create_user_profile_dto(name, email, user_id):
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            name=name,
            email=email,
            user_id=user_id
        )
        return user_profile_dto

    def _validate_values(self, roles, teams, company):
        self._validate_roles(roles)
        self._validate_teams(teams)
        self._validate_company(company)

    def _validate_roles(self, roles):
        are_valid = self.storage.validate_role_ids(role_ids=roles)
        are_not_valid = not are_valid
        if are_not_valid:
            raise RoleIdsAreInvalid()

    def _validate_teams(self, teams):
        are_valid = self.storage.validate_teams(team_ids=teams)
        are_not_valid = not are_valid
        if are_not_valid:
            raise TeamIdsAreInvalid()

    def _validate_company(self, company):
        is_valid = self.storage.validate_company(company_id=company)
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidCompanyId()
