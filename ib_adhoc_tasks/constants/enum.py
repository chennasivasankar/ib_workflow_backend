import enum


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"


class GroupByType(enum.Enum):
    ASSIGNEE = "ASSIGNEE"
    STAGE = "STAGE"
