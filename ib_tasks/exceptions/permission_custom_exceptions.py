
class UserActionPermissionDenied(Exception):
    def __init__(self, action_id: int):
        self.action_id = action_id


class UserBoardPermissionDenied(Exception):
    def __init__(self, board_id: str):
        self.board_id = board_id