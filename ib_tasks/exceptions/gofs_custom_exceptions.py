from typing import List


class DuplicateGoFIds(Exception):
    def __int__(self, message: str):
        self.message = message


class GOFIdCantBeEmpty(Exception):
    pass


class GOFDisplayNameCantBeEmpty(Exception):
    pass


class GOFReadPermissionsCantBeEmpty(Exception):
    pass


class GOFWritePermissionsCantBeEmpty(Exception):
    pass


class GOFFieldIdsCantBeEmpty(Exception):
    pass


class GoFIDsAlreadyExists(Exception):

    def __init__(self, existing_gof_ids: List[str]):
        self.gof_ids = existing_gof_ids


class InvalidGOFIds(Exception):
    def __int__(self, message: str):
        self.message = message


class InvalidOrdersForGoFs(Exception):
    def __int__(self, message: str):
        self.message = message


class ExistingGoFsNotInGivenData(Exception):
    def __init__(self, message: str):
        self.message = message


class GofsDoesNotExist(Exception):
    def __init__(self, message: str):
        self.message = message


class ExistingGoFsNotInGivenGoFs(Exception):
    def __int__(self, message: str):
        self.message = message


class DuplicateOrderValuesForGoFs(Exception):
    def __init__(self, message: str):
        self.message = message


class DifferentDisplayNamesForSameGOF(Exception):
    pass


class DuplicateReadPermissionRolesForAGoF(Exception):

    def __init__(
            self, duplicate_read_permission_role_ids: List[str],
            gof_id: str
    ):
        self.role_ids = duplicate_read_permission_role_ids
        self.gof_id = gof_id


class DuplicateWritePermissionRolesForAGoF(Exception):

    def __init__(
            self, duplicate_write_permission_role_ids: List[str],
            gof_id: str
    ):
        self.role_ids = duplicate_write_permission_role_ids
        self.gof_id = gof_id


class InvalidGoFIds(Exception):

    def __init__(self, invalid_gof_ids: List[str]):
        self.gof_ids = invalid_gof_ids


class DuplicateSameGoFOrderForAGoF(Exception):

    def __int__(self, gof_id: str, duplicate_same_gof_orders: List[int]):
        self.gof_id = gof_id
        self.same_gof_orders = duplicate_same_gof_orders
