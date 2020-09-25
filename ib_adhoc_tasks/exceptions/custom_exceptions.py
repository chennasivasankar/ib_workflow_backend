class InvalidProjectId(Exception):
    pass


class DuplicateGroupByOrder(Exception):
    pass


class InvalidGroupLimitValue(Exception):
    pass


class InvalidGroupOffsetValue(Exception):
    pass


class InvalidTaskLimitValue(Exception):
    pass


class InvalidTaskOffsetValue(Exception):
    pass


class InvalidTaskTemplateId(Exception):
    pass


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class UserNotAllowedToCreateMoreThanOneGroupByInListView(Exception):
    pass


class UserNotAllowedToCreateMoreThanTwoGroupByInKanbanView(Exception):
    pass

class UserNotExistInProject(Exception):
    pass
