from typing import List


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


class UserAccountAlreadyExistWithThisEmail(Exception):
    pass


class InvalidEmailAddress(Exception):
    pass


class NameShouldNotContainsNumbersSpecCharacters(Exception):
    pass


class InvalidNameLength(Exception):
    pass


class RoleIdsAreInvalid(Exception):
    pass


class RoleIdsAreDuplicated(Exception):
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
    def __init__(self, role_ids: List[str]):
        self.role_ids = role_ids


class UserHasNoAccess(Exception):
    pass


class TeamNameAlreadyExists(Exception):
    def __init__(self, team_name: str):
        self.team_name = team_name


class InvalidTeamId(Exception):
    pass


class CompanyNameAlreadyExists(Exception):
    def __init__(self, company_name: str):
        self.company_name = company_name


class UserNotFound(Exception):
    pass


class UserDoesNotHaveDeletePermission(Exception):
    pass


class InvalidUserId(Exception):
    pass


class DuplicateUserIds(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids


class InvalidUserIds(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids


class InvalidCurrentPassword(Exception):
    pass


class InvalidNewPassword(Exception):
    pass


class CurrentPasswordMismatch(Exception):
    pass


class InvalidCityIds(Exception):
    def __init__(self, city_ids: List[int]):
        self.city_ids = city_ids


class InvalidStateIds(Exception):
    def __init__(self, state_ids: List[int]):
        self.state_ids = state_ids


class InvalidCountryIds(Exception):
    def __init__(self, country_ids: List[int]):
        self.country_ids = country_ids


class InvalidProjectId(Exception):
    pass


class TeamNotExistsInGivenProject(Exception):
    pass


class UserNotExistsInGivenTeam(Exception):
    pass


class InvalidTeamIds(Exception):
    def __init__(self, team_ids):
        self.team_ids = team_ids


class InvalidProjectIds(Exception):
    def __init__(self, project_ids):
        self.project_ids = project_ids


class InvalidUserIdsForProject(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids


class InvalidRoleIdsForProject(Exception):
    def __init__(self, role_ids: List[str]):
        self.role_ids = role_ids


class InvalidLevelHierarchyOfTeam(Exception):
    pass