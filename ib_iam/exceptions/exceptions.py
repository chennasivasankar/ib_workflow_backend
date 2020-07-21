class UserIsNotAdminException(Exception):
    pass


class InvalidOffsetValueException(Exception):
    pass


class InvalidLimitValueException(Exception):
    pass


class OffsetValueIsGreaterthanLimitValueException(Exception):
    pass


class UserAccountAlreadyExistWithThisEmail(Exception):
    pass


class GivenNameIsEmptyException(Exception):
    pass


class InvalidEmailAddressException(Exception):
    pass


class NameShouldNotContainsNumbersSpecCharactersException(Exception):
    pass


class RoleIdsAreInvalidException(Exception):
    pass


class InvalidCompanyIdException(Exception):
    pass


class TeamIdsAreInvalidException(Exception):
    pass
