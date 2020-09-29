import enum


class GroupByKey(enum.Enum):
    STAGE = "STAGE"
    ASSIGNEE = "ASSIGNEE"
    TITLE = "title"
    START_DATE = "start_date"
    DUE_DATE = "due_date"
    PRIORITY = "priority"


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"


class ActionTypes(enum.Enum):
    NO_VALIDATIONS = "NO_VALIDATIONS"


class Priority(enum.Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class StatusCode(enum.Enum):
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    SUCCESS = 200
    SUCCESS_CREATE = 201
