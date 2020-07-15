from typing import List


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)


class DifferentTemplateName(Exception):
    def __init__(self, existing_template_name: str, template_name: str):
        self.message = \
            "given template name: {} but it is different from the existing template_name: {}".\
            format(template_name, existing_template_name)
        super().__init__(self.message)


class ExistingGoFNotInGivenGoF(Exception):
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
