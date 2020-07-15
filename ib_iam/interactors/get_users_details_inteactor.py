from uuid import uuid4

from ib_iam.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface import StorageInterface


class UserIsNotAdminException(Exception):
    pass


class InvalidOffsetValueException(Exception):
    pass


class InvalidLimitValueException(Exception):
    pass


class OffsetValueIsGreaterthanLimitException(Exception):
    pass


class GetUsersDetails:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_users_details_wrapper(self, user_id: str, offset: int,
                                  limit: int, presenter: PresenterInterface):
        try:
            self.get_users_details(user_id=user_id, offset=offset, limit=limit)
        except UserIsNotAdminException:
            return presenter.raise_user_is_not_admin_exception()
        except InvalidOffsetValueException:
            return presenter.raise_invalid_offset_value_exception()
        except InvalidLimitValueException:
            return presenter.raise_invalid_limit_value_exception()
        except OffsetValueIsGreaterthanLimitException:
            return presenter. \
                raise_offset_value_is_greater_than_limit_exception()

    def get_users_details(self, user_id: str, offset: int, limit: int):

        self._check_and_throw_user_is_admin(user_id=user_id)
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)
        self._validate_offset_and_limit_value_constraints(
            offset=offset, limit=limit)
        # GET USERS' IDS FILTER ONLY USERS EXCLUDE ADMINS
        user_ids = self.storage.get_user_ids()

        # TODO: GET USERS' TEAM DETAILS
        user_teams = self.storage.get_team_details_of_users_bulk(
            user_ids=user_ids)
        # TODO: GET USERS' ROLE DETAILS
        user_roles = self.storage.get_role_details_of_users_bulk(
            user_ids=user_ids)
        # TODO: GET USERS' COMPANY DETAILS
        # TODO: GET USERS' DETAILS FROM iBUSERS


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
            raise OffsetValueIsGreaterthanLimitException()


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



