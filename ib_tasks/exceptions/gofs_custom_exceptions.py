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
