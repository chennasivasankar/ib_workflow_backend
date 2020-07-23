class UserAccountDoesNotExist(Exception):
    pass


class InvalidEmail(Exception):
    pass


class UserIsNotAdmin(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class OffsetValueIsGreaterThanLimitValue(Exception):
    pass


class UserAccountAlreadyExistWithThisEmail(Exception):
    pass


class GivenNameIsEmpty(Exception):
    pass


class InvalidEmailAddress(Exception):
    pass


class NameShouldNotContainsNumbersSpecCharacters(Exception):
    pass


class RoleIdsAreInvalid(Exception):
    pass


class InvalidCompanyId(Exception):
    pass


class TeamIdsAreInvalid(Exception):
    pass


class UserDoesNotExist(Exception):
    pass


class RoleNameIsEmpty(Exception):
    pass


class RoleDescriptionIsEmpty(Exception):
    pass


class RoleIdFormatIsInvalid(Exception):
    pass


class DuplicateRoleIds(Exception):
    pass

