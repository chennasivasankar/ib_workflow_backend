from ib_tasks.constants.enum \
    import PermissionTypes, FieldTypes, Searchable

ALL_ROLES_ID = "ALL_ROLES"
GOF_ORDER_WITH_MINUS_ONE_VALUE = -1

FIELD_TYPES_LIST = [item.value for item in FieldTypes]

SEARCHABLE_VALUES = [item.value for item in Searchable]
VALID_FIELD_TYPES = [item.value for item in FieldTypes]

Permission_Types = [
    (item.value, item.value)
    for item in PermissionTypes
]

Field_Types = [
    (item.value, item.value)
    for item in FieldTypes
]

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value,
    FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value,
    FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

GOOGLE_SHEET_NAME = "Vendor Configuration_v0"
TASK_TEMPLATE_SUB_SHEET_TITLE = "Task Templates"
GOF_SUB_SHEET_TITLE = "GOF"
FIELD_SUB_SHEET_TITLE = "Fields"

UPLOADERS = [
    FieldTypes.IMAGE_UPLOADER.value,
    FieldTypes.FILE_UPLOADER.value
]
