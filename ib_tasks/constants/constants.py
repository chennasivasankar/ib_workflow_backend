from ib_tasks.constants.enum import PermissionTypes, FieldTypes

FIELD_TYPES_LIST = [item.value for item in FieldTypes]


all_roles_id = "ALL_ROLES"

Permission_Types = [
    (item.value, item.value)
    for item in PermissionTypes
]

Field_Types = [
    (item.value, item.value)
    for item in FieldTypes
]

GOOGLE_SHEET_NAME = "FinMan Configuration_Dev_Test"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
