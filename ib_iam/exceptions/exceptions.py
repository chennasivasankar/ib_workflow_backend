class UserIsNotAdminException(Exception):
    pass


class InvalidOffsetValueException(Exception):
    pass


class InvalidLimitValueException(Exception):
    pass


class OffsetValueIsGreaterthanLimitValueException(Exception):
    pass
