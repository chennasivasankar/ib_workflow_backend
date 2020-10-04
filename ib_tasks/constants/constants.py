from ib_tasks.constants.enum import PermissionTypes, FieldTypes, Searchable, \
    Operators, Priority

ALL_ROLES_ID = "ALL_ROLES"
EMPTY_STRING = ""
GOF_ORDER_WITH_MINUS_ONE_VALUE = -1

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

SEARCHABLE_VALUES = [item.value for item in Searchable]

Permission_Types = [(item.value, item.value) for item in PermissionTypes]

OPERATOR_TYPES = [(item.value, item.value) for item in Operators]
OPERATORS = [item.value for item in Operators]


Field_Types = [(item.value, item.value) for item in FieldTypes]

VALID_FIELD_TYPES = [field_type.value for field_type in FieldTypes]

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value, FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value, FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
FIELD_SUB_SHEET_TITLE = "Fields"
GLOBAL_CONSTANTS_SUB_SHEET_TITLE = "Global Constants"

SEARCHABLE_TYPES = [searchable_type.value for searchable_type in Searchable]
UPLOADERS = [FieldTypes.IMAGE_UPLOADER.value, FieldTypes.FILE_UPLOADER.value]

STAGES_AND_ACTIONS_SUB_SHEET = "Stages and Actions "
STAGE_FLOWS_SUB_SHEET = "Stages and Flow"
TASK_CREATION_CONFIG_SUB_SHEET = "Task Creation Config"
PROJECT_FOR_TASK_TEMPLATES_SUB_SHEET = "Project Task Templates"
STAGE_ID_AND_VALUES_SUB_SHEET = "StageID and Values"
STATUS_VARIABLES_SUB_SHEET = "Status Variables"
ROLES_SUB_SHEET = "Roles"
TRANSITION_TEMPLATES_SUB_SHEET = "Transition Templates"

PRIORITY_TYPES = [(item.value, item.value) for item in Priority]

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

STAGE_TASK = "STAGE_TASK"

TASK_DISPLAY_ID = "JGC-{}"

INTEGER_FIELD_TYPES = [
    FieldTypes.NUMBER.value,
    FieldTypes.PHONE_NUMBER.value,
]

NUMERIC_OPERATORS = [
    Operators.GTE.value, Operators.GT.value,
    Operators.LTE.value, Operators.LT.value
]

STRING_OPERATORS = [
    Operators.CONTAINS.value
]

SEARCHABLE_TYPES_WITH_RESPONSE_ID_AS_STRING = [
    Searchable.USER.value
]

ADHOC_TEMPLATE_ID = "ADHOC"

FIELD_TYPE_TEXT_WITH_FIELD_VALUES = [
    FieldTypes.PLAIN_TEXT_CONTENT.value, FieldTypes.HTML_CONTENT.value,
    FieldTypes.MARKDOWN_CONTENT.value
]

TASK_TEMPLATE_TITLE_DEFAULT_NAME = "Title"

PROJECT_COLUMNS = {
    "JGC_DRIVE": "JGCC_SUCCESSFUL_LEAD",
    "APJ": "APJC_CHILD",
    "MAHATMA": "MHTMC_VILLAGES"
}
