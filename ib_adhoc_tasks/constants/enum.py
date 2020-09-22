import enum


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"
import enum


class GroupByType(enum.Enum):
    STAGE = "STAGE"
    ASSIGNEE = "ASSIGNEE"
    FIELD = "FIELD"
