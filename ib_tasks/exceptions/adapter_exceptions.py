from typing import List


class InvalidProjectIdsException(Exception):
    def __init__(self, invalid_project_ids: List[str]):
        self.invalid_project_ids = invalid_project_ids


class UserIsNotInProjectException(Exception):
    pass


class UserIsNotInProjectsException(Exception):

    def __init__(self, project_ids: List[str]):
        self.project_ids = project_ids