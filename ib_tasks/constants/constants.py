from ib_tasks.constants.enum \
    import PermissionTypes, FieldTypes, Searchable

all_roles_id = "ALL_ROLES"

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

SEARCHABLE_VALUES = [item.value for item in Searchable]


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

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value,
    FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value,
    FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

GOOGLE_SHEET_NAME = "FinMan Configuration_Dev_Test"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
FIELD_SUB_SHEET_TITLE = "Fields"

UPLOADERS = [
    FieldTypes.IMAGE_UPLOADER.value,
    FieldTypes.FILE_UPLOADER.value
]


