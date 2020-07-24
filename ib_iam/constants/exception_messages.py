USER_DOES_NOT_HAVE_PERMISSION = (
    "forbidden access, user cannot access",
    "USER_DOES_NOT_HAVE_PERMISSION"
)
INVALID_USER = (
    "invalid user",
    "INVALID_USER"
)

INVALID_OFFSET_VALUE = (
    "given offset value is invalid, less than 0",
    "INVALID_OFFSET_VALUE"
)

INVALID_LIMIT_VALUE = (
    "given limit value is invalid, less than 0",
    "INVALID_LIMIT_VALUE"
)

OFFSET_VALUE_IS_GREATER_THAN_LIMIT = (
    "offset value should be less than or equal to limit",
    "OFFSET_VALUE_IS_GREATER_THAN_LIMIT"
)

EMPTY_NAME_IS_INVALID = (
    "name should not be empty",
    "EMPTY_NAME_IS_INVALID"
)

NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS = (
    "name should not contains special characters and numbers",
    "NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS"
)

INVALID_EMAIL = (
    "given email is invalid",
    "INVALID_EMAIL"
)

USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL = (
    'given email already registered for another account',
    "USER_ACCOUNT_ALREADY_EXIST_FOR_THIS_EMAIL"
)

ROLE_NAME_SHOULD_NOT_BE_EMPTY = (
    "role name should not be empty",
    "ROLE_NAME_SHOULD_NOT_BE_EMPTY"
)

ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY = (
    "role description should not be empty",
    "ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY"
)

DUPLICATE_ROLE_IDS = (
    "can't create roles with duplicate role_ids",
    "DUPLICATE_ROLE_IDS"
)

ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT = (
    "role id should be valid format ex: PAYMENT_POC",
    "ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT"
)

INVALID_ROLE_IDS = (
    "given role ids are invalid",
    "INVALID_ROLE_IDS"
)

INVALID_TEAM_IDS = (
    "given team ids are invalid",
    "INVALID_TEAM_IDS"
)

INVALID_COMPANY_ID = (
    "given company id is invalid",
    "INVALID_COMPANY_ID"
)

USER_DOES_NOT_EXIST = (
    "user is not exist",
    "USER_DOES_NOT_EXIST"
)

CREATE_USER_SUCCESSFULLY = (
    "User created successfully",
    "CREATE_USER_SUCCESSFULLY"
)

EDIT_USER_SUCCESSFULLY = (
    "Edit User successfully",
    "EDIT_USER_SUCCESSFULLY"
)


USER_HAS_NO_ACCESS_FOR_GET_LIST_OF_TEAMS = (
    "User has no access to see teams as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_LIMIT_FOR_GET_LIST_OF_TEAMS = (
    "Given limit is invalid to retrieve list of teams",
    "INVALID_LIMIT"
)

INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS = (
    "Given offset is invalid to retrieve list of teams",
    "INVALID_OFFSET"
)

USER_HAS_NO_ACCESS_FOR_ADD_TEAM = (
    "User has no access to add a team as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM = (
    "Given '%s' is already exists, so choose another",
    "TEAM_NAME_ALREADY_EXISTS"
)
INVALID_USERS_FOR_ADD_TEAM = (
    "Given users are invalid(not found), please check it",
    "INVALID_USERS"
)

DUPLICATE_USERS_FOR_ADD_TEAM = (
    "Given users consists of duplicates, please check it",
    "DUPLICATE_USERS"
)

USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM = (
    "User has no access to update team details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_TEAM_FOR_UPDATE_TEAM = (
    "Given team is invalid(NotFound)",
    "INVALID_TEAM"
)

TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM = (
    "Given '%s' is already exists, so updating name is not possible.",
    "TEAM_NAME_ALREADY_EXISTS"
)

DUPLICATE_USERS_FOR_UPDATE_TEAM = (
    "Given users consists of duplicates, so update is not possible",
    "DUPLICATE_USERS"
)

INVALID_USERS_FOR_UPDATE_TEAM = (
    "Given users are invalid(not found), so update is not possible",
    "INVALID_USERS"
)

USER_HAS_NO_ACCESS_FOR_DELETE_TEAM = (
    "User has no access to delete team details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_TEAM_FOR_DELETE_TEAM = (
    "Given team is invalid(NotFound)",
    "INVALID_TEAM"
)