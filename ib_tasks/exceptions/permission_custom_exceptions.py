
class UserActionPermissionDenied(Exception):
    def __init__(self, action_id: int):
        self.action_id = action_id
