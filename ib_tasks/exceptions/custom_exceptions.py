from typing import List


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


class DuplicatedFieldIds(Exception):
    pass


class InvalidReadPermissionRoles(Exception):
    pass


class InvalidWritePermissionRoles(Exception):
    pass


class DifferentDisplayNamesForSameGOF(Exception):
    pass


class InvalidFieldIds(Exception):

    def __init__(self, invalid_field_ids: List[int]):
        self.invalid_field_ids = invalid_field_ids
