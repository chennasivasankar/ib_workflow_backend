from typing import List
from uuid import uuid4

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.exceptions.exceptions import UserIsNotAdminException, \
    InvalidOffsetValueException, InvalidLimitValueException, \
    OffsetValueIsGreaterthanLimitValueException
from ib_iam.interactors.presenter_interfaces.dtos \
    import CompleteUserDetailsDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class GetUsersDetails:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_users_details_wrapper(self, user_id: str, offset: int,
                                  limit: int, presenter: PresenterInterface):
        try:
            complete_user_details_dtos = self.get_users_details(
                user_id=user_id, offset=offset, limit=limit)
            print(complete_user_details_dtos)
            return presenter.response_for_get_users(complete_user_details_dtos)
        except UserIsNotAdminException:
            return presenter.raise_user_is_not_admin_exception()
        except InvalidOffsetValueException:
            return presenter.raise_invalid_offset_value_exception()
        except InvalidLimitValueException:
            return presenter.raise_invalid_limit_value_exception()
        except OffsetValueIsGreaterthanLimitValueException:
            return presenter. \
                raise_offset_value_is_greater_than_limit_value_exception()

    def get_users_details(self, user_id: str, offset: int,
                          limit: int) -> CompleteUserDetailsDTO:
        self._check_and_throw_user_is_admin(user_id=user_id)
        self._constants_validations(offset=offset, limit=limit)
        user_dtos = self.storage.get_users_who_are_not_admins(offset=offset, limit=limit)
        user_ids = [user_dto.user_id for user_dto in user_dtos]
        company_ids = [user_dto.company_id for user_dto in user_dtos]

        user_team_dtos = self.storage.get_team_details_of_users_bulk(
            user_ids=user_ids)
        user_role_dtos = self.storage.get_role_details_of_users_bulk(
            user_ids=user_ids)
        user_company_dtos = self.storage.get_company_details_of_users_bulk(
            user_ids=user_ids)

        from ib_iam.adapters.user_service import UserService
        user_service = UserService()
        user_profile_dtos = user_service.get_user_profile_bulk(
            user_ids=user_ids)

        return self._convert_complete_user_details_dtos(
            user_team_dtos, user_role_dtos, user_company_dtos,
            user_profile_dtos, len(user_ids))

    @staticmethod
    def _validate_value_and_throw_exception(value: int):
        valid = bool(isinstance(value, int) and value >= 0)
        invalid = not valid
        if invalid:
            return False
        return True

    @staticmethod
    def _validate_offset_and_limit_value_constraints(offset: int, limit: int):
        if offset > limit:
            raise OffsetValueIsGreaterthanLimitValueException()

    def _constants_validations(self, offset: int, limit: int):
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)
        self._validate_offset_and_limit_value_constraints(
            offset=offset, limit=limit)

    def _check_and_throw_user_is_admin(self, user_id: str):
        is_admin = self.storage.validate_user_is_admin(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            raise UserIsNotAdminException()

    def _validate_offset_value_and_throw_exception(self, offset: int):
        if not self._validate_value_and_throw_exception(value=offset):
            raise InvalidOffsetValueException()

    def _validate_limit_value_and_throw_exception(self, limit: int):
        if not self._validate_value_and_throw_exception(value=limit):
            raise InvalidLimitValueException()

    def _convert_complete_user_details_dtos(
            self, user_team_dtos, user_role_dtos,
            user_company_dtos, user_profile_dtos, total_no_of_users):
        complete_user_details_dto = CompleteUserDetailsDTO(
            users=user_profile_dtos,
            teams=user_team_dtos,
            roles=user_role_dtos,
            companies=user_company_dtos,
            total_no_of_users=total_no_of_users
        )
        return complete_user_details_dto


    @staticmethod
    def _get_user_team(user_team_dtos, user_id):
        teams = []
        for team_dto in user_team_dtos:
            if team_dto.user_id == user_id:
                teams.append(team_dto)
        return teams

    @staticmethod
    def _get_user_company(user_company_dtos, user_id):
        for company_dto in user_company_dtos:
            if company_dto.user_id == user_id:
                return company_dto

    @staticmethod
    def _get_profile(user_profile_dtos, user_id):
        for user_profile in user_profile_dtos:
            if user_profile.user_id == user_id:
                return user_profile

    @staticmethod
    def _get_role(user_role_dtos, user_id):
        roles = []
        for user_role_dto in user_role_dtos:
            if user_role_dto.user_id == user_id:
                roles.append(user_role_dto)
        return roles

