from ib_iam.exceptions.exceptions import InvalidOffsetValueException, \
    InvalidLimitValueException, OffsetValueIsGreaterthanLimitValueException


class ValidationMixin:

    def _validate_offset_value_and_throw_exception(self, offset: int):
        if not self._validate_value_and_throw_exception(value=offset):
            raise InvalidOffsetValueException()

    def _validate_limit_value_and_throw_exception(self, limit: int):
        if not self._validate_value_and_throw_exception(value=limit):
            raise InvalidLimitValueException()

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
            raise OffsetValueIsGreaterthanLimitValueException()

    def _constants_validations(self, offset: int, limit: int):
        self._validate_offset_value_and_throw_exception(offset=offset)
        self._validate_limit_value_and_throw_exception(limit=limit)
        self._validate_offset_and_limit_value_constraints(
            offset=offset, limit=limit)
