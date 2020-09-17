from typing import List

from ib_iam.exceptions.custom_exceptions import (
    UserIsNotAdmin, InvalidEmailAddress, InvalidCompanyId, TeamIdsAreInvalid,
    UserDoesNotExist, NameShouldNotContainsNumbersSpecCharacters,
    InvalidNameLength
)
from ib_iam.interactors.dtos.dtos import \
    AddUserDetailsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.edit_user_presenter_interface \
    import EditUserPresenterInterface
from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class EditUserInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            elastic_storage: ElasticSearchStorageInterface
    ):
        self.elastic_storage = elastic_storage
        self.user_storage = user_storage

    def edit_user_wrapper(
            self, admin_user_id: str, user_id: str,
            add_user_details_dto: AddUserDetailsDTO,
            presenter: EditUserPresenterInterface
    ):
        try:
            self.edit_user(
                admin_user_id=admin_user_id, user_id=user_id,
                add_user_details_dto=add_user_details_dto
            )
            response = presenter.edit_user_success_response()
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin_exception()
        except UserDoesNotExist:
            response = presenter.raise_user_does_not_exist()
        except InvalidEmailAddress:
            response = presenter.response_for_invalid_email_exception()
        except InvalidNameLength:
            response = presenter \
                .response_for_invalid_name_length_exception()
        except NameShouldNotContainsNumbersSpecCharacters:
            response = presenter. \
                response_for_name_contains_special_character_exception()
        # except RoleIdsAreInvalid:
        #     response = presenter.response_for_invalid_role_ids_exception()
        except InvalidCompanyId:
            response = presenter.response_for_invalid_company_ids_exception()
        except TeamIdsAreInvalid:
            response = presenter.response_for_invalid_team_ids_exception()
        return response

    def edit_user(
            self, admin_user_id: str, user_id: str,
            add_user_details_dto: AddUserDetailsDTO
    ):
        name = add_user_details_dto.name
        team_ids = add_user_details_dto.team_ids
        # role_ids = add_user_details_dto.role_ids
        company_id = add_user_details_dto.company_id
        email = add_user_details_dto.email

        self._validate_is_user_admin(user_id=admin_user_id)
        self._is_user_exist(user_id=user_id)
        self._validate_name_and_throw_exception(name=name)
        self._validate_email_and_throw_exception(email=email)
        self._validate_values(
            team_ids=team_ids, company_id=company_id
        )
        self._update_user_profile_in_ib_users(
            user_id=user_id, email=email, name=name
        )
        self._update_user_roles_company_roles(
            user_id=user_id, company_id=company_id,
            team_ids=team_ids, name=name
        )
        self.elastic_storage.update_elastic_user(user_id=user_id, name=name)

    @staticmethod
    def _validate_email_and_throw_exception(email: str):
        import re
        from ib_iam.constants.config import EMAIL_VALIDATION_PATTERN
        email_valid_pattern = EMAIL_VALIDATION_PATTERN
        is_invalid_email = not bool(re.match(email_valid_pattern, email))
        if is_invalid_email:
            raise InvalidEmailAddress()

    def _validate_values(
            self, team_ids: List[str], company_id: str
    ):
        # self._validate_role_ids(role_ids=role_ids)
        self._validate_teams(team_ids=team_ids)
        if company_id is not None:
            self._validate_company(company_id=company_id)

    # def _validate_role_ids(self, role_ids: List[str]):
    #     are_valid = self.user_storage.check_are_valid_role_ids(
    #         role_ids=role_ids)
    #     are_not_valid = not are_valid
    #     if are_not_valid:
    #         raise RoleIdsAreInvalid()

    def _validate_teams(self, team_ids: List[str]):
        are_invalid_team_ids = not self.user_storage.check_are_valid_team_ids(
            team_ids=team_ids
        )
        if are_invalid_team_ids:
            raise TeamIdsAreInvalid()

    def _validate_company(self, company_id: str):
        is_not_valid = not self.user_storage.check_is_exists_company_id(
            company_id=company_id
        )
        if is_not_valid:
            raise InvalidCompanyId()

    def _is_user_exist(self, user_id: str):
        is_not_exist = not self.user_storage.is_user_exist(user_id)
        if is_not_exist:
            raise UserDoesNotExist

    @staticmethod
    def _update_user_profile_in_ib_users(
            user_id: str, email: str, name: str
    ):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            name=name, email=email, user_id=user_id
        )
        service_adapter.user_service.update_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)

    def _update_user_roles_company_roles(
            self, user_id: str, company_id: str,
            team_ids: List[str], name: str
    ):
        # self._remove_existing_teams_and_roles_of_user(user_id)
        self.user_storage.remove_teams_for_user(user_id)
        self._assign_teams_and_roles_and_company_to_user(
            company_id, team_ids, user_id, name
        )

    def _assign_teams_and_roles_and_company_to_user(
            self, company_id: str, team_ids: List[str],
            user_id: str, name: str
    ):
        # db_role_ids = self.user_storage.get_role_objs_ids(role_ids)
        # self.user_storage.add_roles_to_the_user(
        #     user_id=user_id, role_ids=db_role_ids)
        self.user_storage.add_user_to_the_teams(
            user_id=user_id, team_ids=team_ids
        )
        self.user_storage.update_user_details(
            user_id=user_id, company_id=company_id, name=name
        )

    # def _remove_existing_teams_and_roles_of_user(self, user_id: str):
    #     self.user_storage.remove_roles_for_user(user_id)
    #     self.user_storage.remove_teams_for_user(user_id)
