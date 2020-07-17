class UserHasNoAccess(Exception):
    pass


class InvalidLimit(Exception):
    pass


class InvalidOffset(Exception):
    pass


class DuplicateTeamName(Exception):
    def __init__(self, team_name: str):
        self.team_name = team_name


class InvalidTeamId(Exception):
    pass
