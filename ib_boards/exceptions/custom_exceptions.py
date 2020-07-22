from typing import List


class InvalidBoardId(Exception):
    pass

class InvalidOffsetValue(Exception):
    pass

class InvalidLimitValue(Exception):
    pass

class UserDonotHaveAccess(Exception):
    pass

class InvalidStageIds(Exception):
    def __init__(self, invalid_stage_ids: List[str]):
        self.invalid_stage_ids = invalid_stage_ids
