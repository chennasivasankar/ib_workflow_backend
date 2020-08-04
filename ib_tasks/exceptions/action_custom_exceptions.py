

class InvalidActionException(Exception):
    def __init__(self, action_id: int):
        self.action_id = action_id


class InvalidPresentStageAction(Exception):
    def __init__(self, action_id: int):
        self.action_id = action_id


class InvalidKeyError(Exception):
    pass


class InvalidCustomLogicException(Exception):
    pass