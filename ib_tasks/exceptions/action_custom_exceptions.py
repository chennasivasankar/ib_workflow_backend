class InvalidActionException(Exception):
    def __init__(self, action_id: str):
        self.action_id = action_id
