from ib_tasks.constants.enum \
    import PermissionTypes, FieldTypes, Searchable, Operators

ALL_ROLES_ID = "ALL_ROLES"
GOF_ORDER_WITH_MINUS_ONE_VALUE = -1

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

SEARCHABLE_VALUES = [item.value for item in Searchable]

Permission_Types = [(item.value, item.value) for item in PermissionTypes]

OPERATOR_TYPES = [(item.value, item.value)for item in Operators]

Field_Types = [(item.value, item.value) for item in FieldTypes]

VALID_FIELD_TYPES = [field_type.value for field_type in FieldTypes]

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value, FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value, FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

GOOGLE_SHEET_NAME = "Vendor Configuration_v0 - Test"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
FIELD_SUB_SHEET_TITLE = "Fields"
GLOBAL_CONSTANTS_SUB_SHEET_TITLE = "Global Constants"

SEARCHABLE_TYPES = [searchable_type.value for searchable_type in Searchable]
UPLOADERS = [FieldTypes.IMAGE_UPLOADER.value, FieldTypes.FILE_UPLOADER.value]

STAGES_AND_ACTIONS_SUB_SHEET = "Stages and Actions "
TASK_CREATION_CONFIG_SUB_SHEET = "Task Creation Config"
STAGE_ID_AND_VALUES_SUB_SHEET = "StageID and Values"
STATUS_VARIABLES_SUB_SHEET = "Status Variables"
ROLES_SUB_SHEET = "Roles"

OPERATOR_TYPES = [(item.value, item.value)for item in Operators]
