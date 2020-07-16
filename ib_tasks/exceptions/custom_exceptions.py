from typing import List


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)


class ExistingGoFsNotInGivenGoFs(Exception):
    def __init__(self,
                 gof_of_template_not_in_given_gof: List[str],
                 given_gof_ids: List[str]):
        self.message = \
            "Existing gof ids: {} of template not in given gof ids: {}".\
            format(gof_of_template_not_in_given_gof, given_gof_ids)
        super().__init__(self.message)


class InvalidValueForField(Exception):
    def __init__(self, field: str):
        self.message = "Invalid value for field: {}".format(field)
        super().__init__(self.message)


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
