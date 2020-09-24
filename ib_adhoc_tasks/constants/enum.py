import enum


class GroupByEnum(enum.Enum):
    STAGE = "STAGE"
    ASSIGNEE = "ASSIGNEE"


class GroupByType(enum.Enum):
    STAGE = "STAGE"
    ASSIGNEE = "ASSIGNEE"


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"


class ActionTypes(enum.Enum):
    NO_VALIDATIONS = "NO_VALIDATIONS"


class Priority(enum.Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
