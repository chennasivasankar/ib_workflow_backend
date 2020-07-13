

class InvalidStageIdsException(Exception):
    def __init__(self, stage_ids: List[str]):
        self.stage_ids = stage_ids