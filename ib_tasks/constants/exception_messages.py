EMPTY_GOF_ID_MESSAGE = "GoF id should not be empty"
EMPTY_GOF_NAME_MESSAGE = "GoF name should not be empty"
EMPTY_MAX_COLUMNS_MESSAGE = "GoF max columns should not be empty"
EMPTY_GOF_READ_PERMISSIONS_MESSAGE = "GoF read permissions should not be empty"
EMPTY_WRITE_PERMISSIONS_MESSAGE = "GoF write permissions should not be empty"
EMPTY_FIELD_IDS_MESSAGE = "GoF field ids should not be empty"
DUPLICATED_FIELD_IDS_MESSAGE = "GoF field ids should be unique"
MULTIPLE_DISPLAY_NAMES_FOR_SAME_GOF = \
    "One GoF should not have multiple display names"
GOF_ID_ALREADY_EXISTS = "GoF id already exists"
MAX_COLUMNS_VALUE_MUST_NOT_BE_STRING_MESSAGE = \
    "Max columns should not be a string"
MAX_COLUMNS_VALUE_MUST_BE_POSITIVE_INTEGER_MESSAGE = \
    "Max columns value must be greater than zero"
gof_id_already_exists = "GoF id already exists"
DUPLICATE_GOF_IDS = "Given duplicate gof ids {}"
TEMPLATE_DOES_NOT_EXISTS = "The template with template id: {}, does not exists"
DUPLICATE_CONSTANT_NAMES = "Given duplicate constant names {}"
EXISTING_GLOBAL_CONSTANT_NAMES_NOT_IN_GIVEN_DATA = \
    "Existing constants with constant names: {} of template not in given data"
INVALID_VALUE_FOR_GOF_IDS = "Invalid value for gof_ids, got empty string"
INVALID_ORDERS_FOR_GOFS = \
    "Value for order should not be less than -1, got invalid values for these gof_ids: {}"
EXISTING_GOFS_NOT_IN_GIVEN_DATA = \
    "Existing GoFs of template with gof_ids: {} are not in given data"
GOFS_DOES_NOT_EXIST = "The gofs with gof_ids: {}, does not exists"
INVALID_VALUE_FOR_TEMPLATE_ID = \
    "Invalid value for template id!, template id should not be empty"
INVALID_VALUE_FOR_CONSTANT_NAME = \
    "Invalid value for constant name!, constant name should not be empty"
INVALID_VALUE_FOR_VALUE = \
    "Invalid value for value!, value should not be negative!, but given value is: {}"
INVALID_VALUE_FOR_TEMPLATE_NAME = \
    "Invalid value for template name!, template name should not be empty"
MAX_COLUMNS_VALUE_MUST_BE_INTEGER = \
    "Max columns should be a integer value"
INVALID_READ_PERMISSION_ROLES = "Invalid Read Permission roles:"
INVALID_WRITE_PERMISSION_ROLES = "Invalid Write Permission roles:"

DUPLICATE_ORDER_VALUES_FOR_GOFS = \
    "Given duplicate order values {}! Gof orders of a template should be unique"
INVALID_TYPE_FOR_ORDER = "Given value for order: {} is not an integer"
INVALID_TYPE_FOR_VALUE = "Given value for order: {} is not an integer"
TASK_TEMPLATES_DOES_NOT_EXISTS = ("No Task Templates are exists",
                                  "TASK_TEMPLATES_DOES_NOT_EXISTS")
INVALID_GOF_IDS_EXCEPTION_MESSAGE = "Invalid values for gof_ids {}"
EMPTY_VALUE_FOR_FIELD_ID = "Field ids shouldn't be empty"
EMPTY_VALUE_FOR_READ_PERMISSIONS = "Read Permission roles shouldn't be empty for these fields ids {}"
DUPLICATED_VALUES_FOR_READ_PERMISSIONS = "Repeated roles for read permissions for these fields {}"
DUPLICATED_VALUES_FOR_WRITE_PERMISSIONS = "Repeated roles for write permissions for these fields {}"
EMPTY_VALUE_FOR_WRITE_PERMISSIONS = "Write Permission roles shouldn't be empty for these fields ids {}"
INVALID_FIELDS_DISPLAY_NAMES = "Invalid fields display names for these field ids {}"
INVALID_VALUES_FOR_FIELD_TYPES = "Field Types should be one of these {} for these field_ids {}"
DUPLICATION_OF_FIELD_IDS = "These are duplicated field ids {}"
EMPTY_VALUE_FOR_FIELD_VALUE = "Field values shouldn't be empty for this field id {}"
DUPLICATION_OF_FIELD_VALUES = "Duplication of Field values for this field {}"
INVALID_JSON = "Field values contains invalid json for these field_id = {}"
EMPTY_VALUE_FOR_GOF_NAMES = "GoF names for field values shouldn't be empty for this field id = {}"
DUPLICATED_OF_GOF_NAMES_FOR_FIELD_VALUES = "Duplication of gof names for field values of this field = {}"
ALLOWED_FORMAT_EMPTY_VALUES_EXCEPTION = "Allowed formats for these field id shouldn't be empty = {}"
FIELD_DUPLICATION_OF_ALLOWED_FORMATS = "Duplication of values for allowed formats = {}"
EMPTY_VALUES_FOR_ALLOWED_FORMATS = "Allowed formats shouldn't contain empty values for this filed_id = {}"
INVALID_VALUE_FOR_SEARCHABLE = "Searchable value should be one of these  {} for this field_id {}"

DUPLICATE_FIELD_IDS = ["duplicate field ids: {}", "DUPLICATE_FIELD_IDS"]

INVALID_TASK_TEMPLATE_IDS = [
    "invalid task template ids: {}", "INVALID_TASK_TEMPLATE_IDS"
]

INVALID_GOF_IDS = ["invalid gof ids: {}", "INVALID_GOF_IDS"]

INVALID_FIELD_IDS = ["invalid field ids: {}", "INVALID_FIELD_IDS"]

USER_DO_NOT_HAVE_ACCESS = [
    "User do not have access to the action: {}", "USER_DO_NOT_HAVE_ACCESS"
]

USER_DO_NOT_HAVE_BOARD_ACCESS = [
    "User do not have access to the board: {}", "USER_DO_NOT_HAVE_ACCESS"
]

EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD = [
    "got empty value in plain text field for field id: {}",
    "EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD"
]
LIMIT_SHOULD_BE_GREATER_THAN_ZERO = ("Limit value should be greater than zero",
                                     "LIMIT_SHOULD_BE_GREATER_THAN_ZERO")

OFFSET_SHOULD_BE_GREATER_THAN_ZERO = (
    "Offset value should be greater than zero",
    "OFFSET_SHOULD_BE_GREATER_THAN_ZERO")

OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE = (
    "Offset should be greater than or equal to minus one",
    "OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE")

INVALID_TASK_ID = [
    "invalid task id is: {}, please send valid task id", "INVALID_TASK_ID"
]

INVALID_BOARD_ID = [
    "invalid board id is: {}, please send valid board id", "INVALID_BOARD_ID"
]

INVALID_ACTION_ID = [
    "invalid action id is: {}, please send valid action id",
    "INVALID_ACTION_ID"
]

EMPTY_STAGE_IDS_ARE_INVALID = [
    "Stage Ids list should not be empty", "EMPTY_STAGE_IDS_ARE_INVALID"
]

INVALID_PHONE_NUMBER_VALUE = (
    "Invalid value for phone number: {} for field: {}",
    "INVALID_PHONE_NUMBER_VALUE")
INVALID_EMAIL = ("Invalid value for email: {} for field: {}", "INVALID_EMAIL")
INVALID_URL = ("Invalid value for url: {} for field: {}", "INVALID_URL")
NOT_A_STRONG_PASSWORD = (
    "Given a weak password: {} for field: {}! Try with atleast 8 characters including special characters",
    "NOT_A_STRONG_PASSWORD")
INVALID_NUMBER_VALUE = (
    "Invalid number: {} for field: {}! Number should only consists digits",
    "INVALID_NUMBER_VALUE")
INVALID_FLOAT_VALUE = ("Invalid float value: {} for field: {}!",
                       "INVALID_FLOAT_VALUE")
INVALID_VALUE_FOR_DROPDOWN = (
    "Invalid dropdown value: {} for field: {}! Try with these dropdown values: {}",
    "INVALID_VALUE_FOR_DROPDOWN")
INCORRECT_NAME_IN_GOF_SELECTOR_FIELD = (
    "Invalid gof_id: {} for field: {}! Try with these gof_id values: {}",
    "INCORRECT_GOF_ID_IN_GOF_SELECTOR_FIELD")
INCORRECT_RADIO_GROUP_CHOICE = (
    "Invalid radio group choice: {} for field: {}! Try with these valid options: {}",
    "INCORRECT_RADIO_GROUP_CHOICE")
INCORRECT_CHECK_BOX_OPTIONS_SELECTED = (
    "Invalid check box options selected: {} for field: {}! Try with these valid options: {}",
    "INCORRECT_CHECK_BOX_OPTIONS_SELECTED")
INCORRECT_MULTI_SELECT_OPTIONS_SELECTED = (
    "Invalid multi select options selected: {} for field: {}! Try with these valid options: {}",
    "INCORRECT_MULTI_SELECT_OPTIONS_SELECTED")
INCORRECT_MULTI_SELECT_LABELS_SELECTED = (
    "Invalid multi select labels selected: {} for field: {}! Try with these valid options: {}",
    "INCORRECT_MULTI_SELECT_LABELS_SELECTED")
INVALID_DATE_FORMAT = (
    "given invalid format for date: {} for field: {}! Try with this format: {}",
    "INVALID_DATE_FORMAT")
INVALID_TIME_FORMAT = (
    "given invalid format for time: {} for field: {}! Try with this format: {}",
    "INVALID_TIME_FORMAT")
INVALID_IMAGE_FORMAT = (
    "Invalid format for an image: {} for field: {}! Try with these formats: {}",
    "INVALID_IMAGE_FORMAT")
INVALID_IMAGE_URL = ("Invalid url for an image: {} for field: {}!",
                     "INVALID_IMAGE_URL")
INVALID_FILE_URL = ("Invalid url for a file: {} for field: {}!",
                    "INVALID_FILE_URL")
INVALID_NAME_IN_GOF_SELECTOR_FIELD = (
    "Invalid gof selector name: {} in gof_selector_field!",
    "INVALID_NAME_IN_GOF_SELECTOR_FIELD")
INVALID_FILE_FORMAT = (
    "Invalid format for a file: {} for field: {}! Try with these formats: {}",
    "INVALID_FILE_FORMAT")
EMPTY_VALUE_FOR_REQUIRED_FIELD = [
    "Given Empty value for the required field of field_id: {}! Required field should not be empty",
    "EMPTY_VALUE_FOR_REQUIRED_FIELD"
]

TASK_CREATED_SUCCESSFULLY = ("task created or updated successfully",
                             "TASK_CREATED_SUCCESSFULLY")

INVALID_TASK_JSON = ("Task Json should not be empty", "INVALID_TASK_JSON")

INVALID_GOFS_OF_TASK_TEMPLATE = (
    "invalid gofs {}  given to the task template {}",
    "INVALID_GOFS_OF_TASK_TEMPLATE")

DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF = ("gof id {} has duplicate field ids {}",
                                    "DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF")

INVALID_FIELDS_OF_TASK_TEMPLATE = ("invalid fields {}  given to the gof {}",
                                   "INVALID_FIELDS_OF_TASK_TEMPLATE")

USER_NEEDS_GOF_WRITABLE_PERMISSION = (
    "user {} needs write access on gof {}, because user does not have {} roles",
    "USER_NEEDS_GOF_WRITABLE_PERMISSION")

USER_NEEDS_FILED_WRITABLE_PERMISSION = (
    "user {} needs write access on field {}, because user does not have {} roles",
    "USER_NEEDS_FILED_WRITABLE_PERMISSION")
INVALID_FILTER_ID = ('invalid filter id', 'INVALID_FILTER_ID')

USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS = (
    'user not have access to update the filter status',
    'USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS')
TASK_ID_DOESNT_EXIST = ("Task id doesnt exist, please send valid task id",
                        "TASK_ID_DOESNT_EXIST")

USER_NOT_HAVE_PERMISSIONS_TO_FIELDS = ('user not have access to fields',
                                       'USER_NOT_ACCESS_TO_FIELDS')
FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE = (
    'fields not belongs to task template: {}',
    'FIELDS_NOT_BELONGS_TO_TASK_TEMPLATE')

USER_NOT_HAVE_PERMISSIONS_TO_UPDATE = (
    'user not have access to update the filter',
    'USER_NOT_HAVE_PERMISSIONS_TO_UPDATE')

USER_NOT_HAVE_PERMISSIONS_TO_DELETE = (
    'user not have access to delete the filter',
    'USER_NOT_HAVE_PERMISSIONS_TO_DELETE')
DUPLICATE_STAGE_IDS = ("Duplicate stage ids that you have sent are: {},"
                       "please send unique stage ids", "DUPLICATE_STAGE_IDS")
TRANSITION_TEMPLATE_DOES_NOT_EXISTS = (
    "Given invalid transition template Id: {}, that does not exists",
    "TRANSITION_TEMPLATE_DOES_NOT_EXISTS")

DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF = (
    "duplicate same gof orders given for gof {}, duplicates are {}",
    "DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF")

INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID = (
    "please give a valid transition checklist template id, {} is invalid \
    transition checklist template id",
    "INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID")

INVALID_STAGE_ID = ("please give a valid stage id, {} is invalid stage id",
                    "INVALID_STAGE_ID")

TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION = (
    "given transition template id {} is not linked to given stage id {} and \
    action id {}", "TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION")

INVALID_STAGE_IDS = ("Invalid stage ids that you have sent are: {},"
                     "please send valid stage ids", "INVALID_STAGE_IDS")
STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE = (
    "Stage ids with invalid permission of assignees that you have sent are: {},"
    "please assign valid assignees for stages",
    "STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE")

INVALID_STAGE_IDS_FOR_TASK = "Invalid stage_ids : {} for the task_id: {}"
INVALID_KEY_ERROR = ("invalid key error", "INVALID_KEY_ERROR")

INVALID_CUSTOM_LOGIC = ("invalid custom logic", "INVALID_CUSTOM_LOGIC")

PATH_NOT_FOUND = ("path not found", "PATH_NOT_FOUND")
METHOD_NOT_FOUND = ("method not found", "METHOD_NOT_FOUND")

INVALID_DUE_TIME_FORMAT = (
    "{} has invalid due time format, time format should be HH:MM:SS",
    "INVALID_DUE_TIME_FORMAT"
)
START_DATE_IS_AHEAD_OF_DUE_DATE = (
    "given start date {} is ahead of given due date {} ",
    "START_DATE_IS_AHEAD_OF_DUE_DATE"
)

DUE_DATE_IS_BEHIND_START_DATE = (
    "given due date {} is behind given start date {}",
    "DUE_DATE_IS_BEHIND_START_DATE"
)

DUE_TIME_HAS_EXPIRED_FOR_TODAY = (
    "give due time {} has expired for today date",
    "DUE_TIME_HAS_EXPIRED_FOR_TODAY"
)

DUE_DATE_HAS_EXPIRED = (
    "given due date {} has expired",
    "DUE_DATE_HAS_EXPIRED"
)

INVALID_STAGES_FOR_TASK = (
    "invalid stages for task",
    "INVALID_STAGE_IDS_FOR_TASK"
)
INVALID_TASK_DISPLAY_ID = (
    "{} is invalid task_id send valid task_id",
    "INVALID_TASK_ID"
)
<<<<<<< HEAD

INVALID_PRESENT_STAGE_ACTION = (
    "{} is invalid present stage action",
    "INVALID_PRESENT_STAGE_ACTION"
)
=======
INVALID_TASK_DB_ID = (
    "Invalid task id",
    "INVALID_TASK_ID"
)
>>>>>>> 50fc05f65c2d10f12d0ad6bcf80c68bedac30471
