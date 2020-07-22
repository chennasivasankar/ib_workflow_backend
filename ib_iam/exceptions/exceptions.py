class UserIsNotAdmin(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class OffsetValueIsGreaterthanLimitValue(Exception):
    pass


class UserAccountAlreadyExistWithThisEmail(Exception):
    pass


class GivenNameIsEmpty(Exception):
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


class UserDoesNotExist(Exception):
    pass
