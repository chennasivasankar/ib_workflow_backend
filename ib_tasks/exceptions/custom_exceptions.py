
from typing import Dict

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