from ib_iam.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueIsGreaterThanLimitValue, GivenNameIsEmpty, \
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

    @staticmethod
    def _validate_offset_and_limit_value_constraints(offset: int, limit: int):
        if offset >= limit:
            raise OffsetValueIsGreaterThanLimitValue()

    def _constants_validations(self, offset: int, limit: int):
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)
        self._validate_offset_and_limit_value_constraints(
            offset=offset, limit=limit)

    def _validate_string(self, value):
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
