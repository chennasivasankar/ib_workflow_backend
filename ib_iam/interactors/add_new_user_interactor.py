from ib_iam.exceptions.custom_exceptions import (
    UserIsNotAdmin, InvalidEmailAddress,
    UserAccountAlreadyExistWithThisEmail,
    NameShouldNotContainsNumbersSpecCharacters, RoleIdsAreInvalid,
    InvalidCompanyId, TeamIdsAreInvalid, InvalidNameLength
)
from ib_iam.interactors.dtos.dtos import \
    UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
    import AddUserPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class AddNewUserInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_new_user_wrapper(
            self, user_id: str,
            user_details_with_team_role_and_company_ids_dto \
                    : UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO,
            presenter: AddUserPresenterInterface):
        try:
            self.add_new_user(
                user_id=user_id,
                user_details_with_team_role_and_company_ids_dto \
                    =user_details_with_team_role_and_company_ids_dto)
            response = presenter.user_created_response()
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        except InvalidNameLength:
            response = presenter \
                .raise_name_minimum_length_should_be_equal_or_more_than()
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

    def add_new_user(self, user_id: str,
                     user_details_with_team_role_and_company_ids_dto):
        self._validate_add_new_user_details(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto)
        email = user_details_with_team_role_and_company_ids_dto.email
        name = user_details_with_team_role_and_company_ids_dto.name
        company_id = user_details_with_team_role_and_company_ids_dto.company_id
        team_ids = user_details_with_team_role_and_company_ids_dto.team_ids
        role_ids = user_details_with_team_role_and_company_ids_dto.role_ids
        new_user_id = self._create_user_in_ib_users(email, name)
        role_obj_ids = self.user_storage.get_role_objs_ids(role_ids=role_ids)
        is_admin = False

        self.user_storage.create_user(
            is_admin=is_admin, company_id=company_id,
            user_id=new_user_id, name=name)
        self.user_storage.add_user_to_the_teams(
            user_id=new_user_id, team_ids=team_ids)
        self.user_storage.add_roles_to_the_user(
            user_id=new_user_id, role_ids=role_obj_ids)

    def _validate_add_new_user_details(
            self, user_id,
            user_details_with_team_role_and_company_ids_dto:
            UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO):
        name = user_details_with_team_role_and_company_ids_dto.name
        email = user_details_with_team_role_and_company_ids_dto.email
        role_ids = user_details_with_team_role_and_company_ids_dto.role_ids
        team_ids = user_details_with_team_role_and_company_ids_dto.team_ids
        company_id = user_details_with_team_role_and_company_ids_dto.company_id
        self._validate_is_user_admin(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        self._validate_roles(role_ids=role_ids)
        self._validate_teams(team_ids=team_ids)
        self._validate_company_id(company_id=company_id)

    def _create_user_in_ib_users(self, email, name):
        new_user_id = self._create_user_account_with_email(email=email)
        self._create_user_profile(user_id=new_user_id, email=email, name=name)
        return new_user_id

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

    def _validate_roles(self, role_ids):
        are_valid = self.user_storage.check_are_valid_role_ids(
            role_ids=role_ids)
        are_not_valid = not are_valid
        if are_not_valid:
            raise RoleIdsAreInvalid()

    def _validate_teams(self, team_ids):
        are_valid = self.user_storage.check_are_valid_team_ids(
            team_ids=team_ids)
        are_not_valid = not are_valid
        if are_not_valid:
            raise TeamIdsAreInvalid()

    def _validate_company_id(self, company_id):
        is_valid = self.user_storage.check_is_exists_company_id(
            company_id=company_id)
        is_not_valid = not is_valid
        if is_not_valid:
            raise InvalidCompanyId()
