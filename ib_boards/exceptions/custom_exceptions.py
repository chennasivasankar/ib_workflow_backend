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


class InvalidTaskIdInListViewFields(Exception):
    def __init__(self, task_ids: List[str]):
        self.task_ids = task_ids


class InvalidTaskIdInKanbanViewFields(Exception):
    def __init__(self, task_ids: List[str]):
        self.task_ids = task_ids


class EmptyValuesForTaskTemplateStages(Exception):
    pass


class EmptyValuesForTaskSummaryFields(Exception):
    pass


class EmptyValuesForTaskListViewFields(Exception):
    pass


class EmptyValuesForTaskKanbanViewFields(Exception):
    pass


class InvalidBoardId(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidProjectId(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class UserDonotHaveAccess(Exception):
    pass


class TaskTemplateStagesNotBelongsToTaskTemplateId(Exception):
    pass


class TaskSummaryFieldsNotBelongsToTaskTemplateId(Exception):
    pass


class TaskListViewFieldsNotBelongsToTaskTemplateId(Exception):
    pass


class TaskKanbanViewFieldsNotBelongsToTaskTemplateId(Exception):
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
    def __init__(self, column_id: str):
        self.column_id = column_id


class UserDoNotHaveAccessToBoards(Exception):
    pass


class UserDoNotHaveAccessToColumn(Exception):
    pass


class InvalidBoardIds(Exception):
    def __init__(self, board_ids: List[str]):
        self.board_ids = board_ids


class InvalidBoardId(Exception):
    pass


class InvalidColumnId(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class UserDonotHaveAccess(Exception):
    pass


class OffsetValueExceedsTotalTasksCount(Exception):
    pass


class InvalidStageIds(Exception):
    def __init__(self, stage_ids: List[str]):
        self.stage_ids = stage_ids


class DuplicateValuesInColumnDisplayOrder(Exception):
    def __init__(self, display_order_values: List[int]):
        self.display_order_values = display_order_values


class InvalidTemplateFields(Exception):
    def __init__(self, invalid_field_template_ids: List[str]):
        self.invalid_field_template_ids = invalid_field_template_ids


class InvalidFormatException(Exception):
    def __init__(self, valid_format: str):
        self.valid_format = valid_format


class InvalidBoardIdsException(Exception):
    def __init__(self, invalid_board_ids: List[str]):
        self.invalid_board_ids = invalid_board_ids
