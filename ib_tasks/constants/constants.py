from ib_tasks.constants.enum \
    import PermissionTypes, FieldTypes, Searchable

all_roles_id = "ALL_ROLES"
LIMIT_VALUE = 10
OFFSET_VALUE = 0

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

SEARCHABLE_VALUES = [item.value for item in Searchable]

Permission_Types = [(item.value, item.value) for item in PermissionTypes]

Field_Types = [(item.value, item.value) for item in FieldTypes]

VALID_FIELD_TYPES = [field_type.value for field_type in FieldTypes]

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value, FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value, FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

GOOGLE_SHEET_NAME = "FinMan Configuration_Dev_Test"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
FIELD_SUB_SHEET_TITLE = "Fields"

SEARCHABLE_TYPES = [searchable_type.value for searchable_type in Searchable]
UPLOADERS = [FieldTypes.IMAGE_UPLOADER.value, FieldTypes.FILE_UPLOADER.value]

STAGES_AND_ACTIONS_SUB_SHEET = "PR - Stages and Actions "
TASK_CREATION_CONFIG_SUB_SHEET = "PR-Task Creation Config"
STAGE_ID_AND_VALUES_SUB_SHEET = "PR - StageID and Values"
STATUS_VARIABLES_SUB_SHEET = "PR - Status Variables"
