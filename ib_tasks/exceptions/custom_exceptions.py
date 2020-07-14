from typing import List


class DuplicateGroupOfFields(Exception):
    def __init__(self, group_of_fields_ids: List[str]):
        self.message = "Given Duplicate group_of_fields_ids: {}".format(
            group_of_fields_ids
        )
        super().__init__(self.message)


class DifferentTemplateName(Exception):
    def __init__(self, template_name: str):
        self.message = \
            "Template already exists! you have given different template name: {}". \
                format(template_name)
        super().__init__(self.message)


class TemplateNotExists(Exception):
    pass


class ExistingGroupOfFieldsNotInGivenGroupOfFields(Exception):
    def __init__(self, group_of_fields_ids: List[str]):
        self.message = \
            "Existing group of fields ids not in given group of fields ids: {}". \
                format(group_of_fields_ids)
        super().__init__(self.message)


class InvalidOrder(Exception):
    def __init__(self, group_of_fields_id: str, order: int):
        self.message = "Invalid Order: {} for group_of_fields_id: {}".format(
            order, group_of_fields_id
        )
        super().__init__(self.message)


class InvalidValueForField(Exception):
    def __init__(self, field: str):
        self.message = "Invalid for field: {}".format(field)
        super().__init__(self.message)
