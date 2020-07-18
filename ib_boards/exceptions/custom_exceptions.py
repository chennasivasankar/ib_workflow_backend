from typing import List


class InvalidBoardDisplayName(Exception):
    def __init__(self, board_id: str):
        self.board_id = board_id


class DuplicateColumnIds(Exception):
    def __init__(self, column_ids: List[str]):
        self.column_ids = column_ids


class InvalidColumnDisplayName(Exception):
    def __init__(self, column_ids: List[str]):
        self.column_ids = column_ids


class InvalidTaskTemplateIdInStages(Exception):
    def __init__(self, task_template_ids: List[str]):
        self.task_template_ids = task_template_ids


class InvalidTaskIdInSummaryFields(Exception):
    def __init__(self, task_ids: List[str]):
        self.task_ids = task_ids


class EmptyValuesForTaskTemplateStages(Exception):
    pass


class EmptyValuesForTaskSummaryFields(Exception):
    pass


class TaskTemplateStagesNotBelongsToTaskTemplateId(Exception):
    pass


class TaskSummaryFieldsNotBelongsToTaskTemplateId(Exception):
    pass


class DuplicateStagesInTaskTemplateStages(Exception):
    def __init__(self, duplicate_stages: List[str]):
        self.duplicate_stages = duplicate_stages


class DuplicateSummaryFieldsInTask(Exception):
    def __init__(self, duplicate_fields: List[str]):
        self.duplicate_fields = duplicate_fields


class InvalidUserRoles(Exception):
    def __init__(self, user_role_ids: List[str]):
        self.user_role_ids = user_role_ids


class ColumnIdsAssignedToDifferentBoard(Exception):
    def __init__(self, column_ids: List[str]):
        self.column_ids = column_ids
