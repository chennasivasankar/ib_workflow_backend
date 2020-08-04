from typing import List
from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, GivenNameIsEmpty, \
    NameShouldNotContainsNumbersSpecCharacters


class ValidationMixin:

    def _validate_offset_value_and_throw_exception(self, offset: int):
        if not self._validate_value_and_throw_exception(value=offset):
            raise InvalidOffsetValue()

    def _validate_limit_value_and_throw_exception(self, limit: int):
        if not self._validate_value_and_throw_exception(value=limit):
            raise InvalidLimitValue()

    @staticmethod
    def _validate_value_and_throw_exception(value: int):
        valid = bool(isinstance(value, int) and value >= 0)
        invalid = not valid
        if invalid:
            return False
        return True

    def _constants_validations(self, offset: int, limit: int):
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)

    @staticmethod
    def _validate_string(value):
        valid = bool(isinstance(value, str) and value != "")
        invalid = not valid
        if invalid:
            return False
        return True

    def _validate_name_and_throw_exception(self, name: str):
        if not self._validate_string(value=name):
            raise GivenNameIsEmpty()
        self._check_name_contains_special_characters_and_throw_exception(name)

    @staticmethod
    def _check_name_contains_special_characters_and_throw_exception(name):
        if not name.isalpha():
            raise NameShouldNotContainsNumbersSpecCharacters()

    def _validate_is_user_admin(self, user_id: str):
        is_admin = self.user_storage.is_user_admin(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
            raise UserIsNotAdmin()

    def _validate_duplicate_or_invalid_users(self, user_ids):
        self._validate_is_duplicate_users_exists(user_ids=user_ids)
        self._validate_is_invalid_users_exists(user_ids=user_ids)

    @staticmethod
    def _validate_is_duplicate_users_exists(user_ids: List[str]):
        is_duplicate_user_ids_exist = len(user_ids) != len(set(user_ids))
        if is_duplicate_user_ids_exist:
            import collections
            user_ids_with_count_dict = collections.Counter(user_ids)
            duplicate_user_ids_list = [
                user_id
                for user_id, user_id_count in user_ids_with_count_dict.items()
                if user_id_count > 1
            ]
            from ib_iam.exceptions.custom_exceptions import DuplicateUserIds
            raise DuplicateUserIds(user_ids=duplicate_user_ids_list)

    def _validate_is_invalid_users_exists(self, user_ids: List[str]):
        user_ids_from_db = \
            self.user_storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids)
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            invalid_user_ids_list = list(set(user_ids) - set(user_ids_from_db))
            from ib_iam.exceptions.custom_exceptions import InvalidUserIds
            raise InvalidUserIds(user_ids=invalid_user_ids_list)
