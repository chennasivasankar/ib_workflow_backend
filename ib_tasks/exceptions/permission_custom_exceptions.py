from typing import List


class UserActionPermissionDenied(Exception):
    def __init__(self, action_id: int):
        self.action_id = action_id


class UserBoardPermissionDenied(Exception):
    def __init__(self, board_id: str):
        self.board_id = board_id


class UserNeedsGoFWritablePermission(Exception):
    def __init__(self, user_id: str, gof_id: str,
                 required_user_roles: List[str]):
        self.user_id = user_id
        self.gof_id = gof_id
        self.required_roles = required_user_roles


class UserNeedsFieldWritablePermission(Exception):
    def __init__(self, user_id: str, field_id: str,
                 required_user_roles: List[str]):
        self.user_id = user_id
        self.field_id = field_id
        self.required_roles = required_user_roles


class InvalidUserIdException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id
