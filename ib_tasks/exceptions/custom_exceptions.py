from typing import List


class DuplicateGoFIds(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = "Given duplicate gof ids {}".format(gof_ids)
        super().__init__(self.message)


class DifferentTemplateName(Exception):
    def __init__(self, template_name: str):
        self.message = \
            "Template already exists! you have given different template name: {}". \
                format(template_name)
        super().__init__(self.message)


class TemplateNotExists(Exception):
    pass


class ExistingGoFNotInGivenGoF(Exception):
    def __init__(self, gof_ids: List[str]):
        self.message = \
            "Existing gof ids not in given gof ids: {}".format(gof_ids)
        super().__init__(self.message)


class InvalidValueForField(Exception):
    def __init__(self, field: str):
        self.message = "Invalid for field: {}".format(field)
        super().__init__(self.message)
