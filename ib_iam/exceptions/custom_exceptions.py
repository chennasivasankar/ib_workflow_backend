class UserHasNoAccess(Exception):
    pass


class InvalidLimit(Exception):
    pass


class InvalidOffset(Exception):
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
