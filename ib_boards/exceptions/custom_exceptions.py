from typing import List


class DuplicateBoardIds(Exception):
    def __init__(self, board_ids: List[str]):
        self.board_ids = board_ids


class InvalidBoardDisplayName(Exception):
    def __init__(self, board_id: str):
        self.board_id = board_id


class DuplicateColumnIds(Exception):
    def __init__(self, column_ids: List[str]):
        self.column_ids = column_ids


class InvalidColumnDisplayName(Exception):
    def __init__(self, column_id: str):
        self.column_id = column_id


class InvalidJsonForTaskTemplateStages(Exception):
    pass


class InvalidTaskTemplateIdInStages(Exception):
    def __init__(self, task_template_id: str):
        self.task_template_id = task_template_id


class InvalidJsonForTaskTemplateSummaryFields(Exception):
    pass


class EmptyValuesForTaskTemplateStages(Exception):
    pass


class TaskTemplateStagesNotBelongsToTastTemplateId(Exception):
    pass


class DuplicateStagesInTaskTemplateStages(Exception):
    def __init__(self, duplicate_stages: List[str]):
        self.duplicate_stages = duplicate_stages