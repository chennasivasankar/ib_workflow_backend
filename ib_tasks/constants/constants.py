from ib_tasks.constants.enum import PermissionTypes, FieldTypes

all_roles_id = "ALL_ROLES"

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

Permission_Types = [
    (item.value, item.value)
    for item in PermissionTypes
]

Field_Types = [
    (item.value, item.value)
    for item in FieldTypes
]

FIELDS_CSV_FILE_PATH = "/home/ib-developer/Desktop/aws/ib-workflows-backend/ib_tasks/populate/fields.csv"

GOFS_CSV_FILE_PATH = "/home/ib-developer/Desktop/aws/ib-workflows-backend/ib_tasks/populate/gofs.csv"

TASK_TEMPLATES_CSV_FILE_PATH = "/home/ib-developer/Desktop/aws/ib-workflows-backend/ib_tasks/populate/task_templates.csv"
