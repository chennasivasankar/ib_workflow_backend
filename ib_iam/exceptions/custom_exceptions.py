class UserAccountDoesNotExist(Exception):
    pass


class InvalidEmail(Exception):
    pass


class UserIsNotAdmin(Exception):
    pass


class InvalidUser(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
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


class UserHasNoAccess(Exception):
    pass


class TeamNameAlreadyExists(Exception):
    def __init__(self, team_name: str):
        self.team_name = team_name


class InvalidTeam(Exception):
    pass


class InvalidUsers(Exception):
    pass


class DuplicateUsers(Exception):
    pass


class CompanyNameAlreadyExists(Exception):
    def __init__(self, company_name: str):
        self.company_name = company_name


class InvalidCompany(Exception):
    pass

class UserNotFound(Exception):
    pass


class UserDoesNotHaveDeletePermission(Exception):
    pass


class InvalidUserId(Exception):
    pass


class InvalidUserIds(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids
