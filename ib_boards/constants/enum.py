import enum


class StartAction(enum.Enum):
    STAR = "STAR"
    UNSTAR = "UNSTAR"


class ViewType(enum.Enum):
    LIST = "LIST"
    KANBAN = "KANBAN"


class DisplayStatus(enum.Enum):
    HIDE = "HIDE"
    SHOW = "SHOW"
