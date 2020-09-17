from typing import List

from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue


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

    def _validate_pagination_details(self, offset: int, limit: int):
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)

    def _validate_name_and_throw_exception(self, name: str):
        self._validate_is_name_satisfies_minimum_length_constant(name)
        self._check_string_contains_special_characters_except_space_and_throw_exception(
            name)

    @staticmethod
    def _validate_is_name_satisfies_minimum_length_constant(value: str):
        # value = value.replace(" ", "")
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        is_string_not_satisfies_minimum_length = \
            len(value) < MINIMUM_USER_NAME_LENGTH
        if is_string_not_satisfies_minimum_length:
            from ib_iam.exceptions.custom_exceptions import \
                InvalidNameLength
            raise InvalidNameLength

    @staticmethod
    def _check_string_contains_special_characters_except_space_and_throw_exception(
            value: str):
        spaces_removed_string = value.replace(" ", "")
        is_special_characters_and_numbers_not_exists_in_string = \
            not spaces_removed_string.isalpha()
        if is_special_characters_and_numbers_not_exists_in_string:
            from ib_iam.exceptions.custom_exceptions import \
                NameShouldNotContainsNumbersSpecCharacters
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
            from ib_iam.exceptions.custom_exceptions import DuplicateUserIds
            raise DuplicateUserIds

    def _validate_is_invalid_users_exists(self, user_ids: List[str]):
        user_ids_from_db = \
            self.user_storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=user_ids)
        is_invalid_users_found = len(user_ids) != len(user_ids_from_db)
        if is_invalid_users_found:
            from ib_iam.exceptions.custom_exceptions import UserIdsAreInvalid
            raise UserIdsAreInvalid
