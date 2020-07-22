from ib_tasks.constants.enum import PermissionTypes, FieldTypes

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

Permission_Types = [
    (item.value, item.value)
    for item in PermissionTypes
]

Field_Types = [
    (item.value, item.value)
    for item in FieldTypes
]

VALID_FIELD_TYPES = [
    field_type.value
    for field_type in FieldTypes
]

GOOGLE_SHEET_NAME = "FinMan Configuration"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
