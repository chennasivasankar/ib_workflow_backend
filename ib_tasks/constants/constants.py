from ib_tasks.constants.enum \
    import PermissionTypes, FieldTypes, Searchable

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

MULTI_VALUES_INPUT_FIELDS = [
    FieldTypes.DROPDOWN.value,
    FieldTypes.RADIO_GROUP.value,
    FieldTypes.CHECKBOX_GROUP.value,
    FieldTypes.MULTI_SELECT_FIELD.value,
    FieldTypes.MULTI_SELECT_LABELS.value
]

GOOGLE_SHEET_NAME = "FinMan Configuration"

FIELD_SUB_SHEET_TITLE = "Fields"



