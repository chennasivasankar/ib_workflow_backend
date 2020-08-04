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
        is_admin = self.storage.is_user_admin(user_id=user_id)
        is_not_admin = not is_admin
        if is_not_admin:
            from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin
            raise UserIsNotAdmin()
