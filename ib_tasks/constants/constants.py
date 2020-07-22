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

GOOGLE_SHEET_NAME = "FinMan Configuration_Dev_Test"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"

STAGES_AND_ACTIONS_SUB_SHEET = "PR - Stages and Actions "
TASK_CREATION_CONFIG_SUB_SHEET = "PR-Task Creation Config"
STAGE_ID_AND_VALUES_SUB_SHEET = "PR - StageID and Values"
STATUS_VARIABLES_SUB_SHEET = "PR - Status Variables"
