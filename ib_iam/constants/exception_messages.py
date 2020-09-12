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

EMPTY_NAME_IS_INVALID = (
    "name should not be empty",
    "EMPTY_NAME_IS_INVALID"
)

NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS = (
    "name should not contains special characters and numbers",
    "NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS"
)

INVALID_NAME_LENGTH = (
    "Name minimum length should be {minimum_name_length} or more",
    "INVALID_NAME_LENGTH"
)

INVALID_EMAIL = (
    "given email is invalid",
    "INVALID_EMAIL"
)

USER_ALREADY_EXIST_WITH_THIS_EMAIL = (
    'given email already registered for another account',
    "USER_ALREADY_EXIST_WITH_THIS_EMAIL"
)

EMAIL_ALREADY_IN_USE = (
    "Email is already in use",
    "EMAIL_ALREADY_IN_USE"
)

ROLE_NAME_SHOULD_NOT_BE_EMPTY = (
    "role display_name should not be empty",
    "ROLE_NAME_SHOULD_NOT_BE_EMPTY"
)

ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY = (
    "role description should not be empty",
    "ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY"
)

DUPLICATE_ROLE_IDS = (
    "can't create roles with duplicate role_ids are {duplicate_role_ids}",
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

DUPLICATE_ROLE_IDS_FOR_UPDATE_USER_PROFILE = (
    "can't create roles with duplicate role_ids",
    "DUPLICATE_ROLE_IDS"
)

INVALID_TEAM_IDS = (
    "given team ids are invalid",
    "INVALID_TEAM_IDS"
)

DUPLICATE_TEAM_IDS = (
    "Given team ids has duplicate entries",
    "DUPLICATE_TEAM_IDS"
)

INVALID_COMPANY_ID = (
    "given company id is invalid",
    "INVALID_COMPANY_ID"
)

USER_DOES_NOT_EXIST = (
    "user is not exist",
    "USER_DOES_NOT_EXIST"
)

USER_DOES_NOT_HAVE_DELETE_PERMISSION = (
    "User does not have delete permission",
    "USER_DOES_NOT_HAVE_DELETE_PERMISSION"
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
INVALID_USER_IDS_FOR_ADD_TEAM = (
    "Given users are not found",
    "INVALID_USER_IDS"
)

DUPLICATE_USER_IDS_FOR_ADD_TEAM = (
    "Duplicate Users has sent, please check it",
    "DUPLICATE_USER_IDS"
)

USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM = (
    "User has no access to update team details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_TEAM_ID_FOR_UPDATE_TEAM = (
    "Given team id is invalid(NotFound)",
    "INVALID_TEAM_ID"
)

TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM = (
    "Given '%s' is already exists, so updating name is not possible.",
    "TEAM_NAME_ALREADY_EXISTS"
)

DUPLICATE_USER_IDS_FOR_UPDATE_TEAM = (
    "Given users '%s' are duplicated, so update is not possible",
    "DUPLICATE_USER_IDS"
)

INVALID_USER_IDS_FOR_UPDATE_TEAM = (
    "Given users '%s' are invalid(not found), so update is not possible",
    "INVALID_USER_IDS"
)

USER_HAS_NO_ACCESS_FOR_DELETE_TEAM = (
    "User has no access to delete team details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_TEAM_ID_FOR_DELETE_TEAM = (
    "Given team is invalid(NotFound)",
    "INVALID_TEAM_ID"
)

USER_HAS_NO_ACCESS_FOR_GET_COMPANIES = (
    "User has no access to see all available companies",
    "USER_HAS_NO_ACCESS"
)

USER_HAS_NO_ACCESS_FOR_ADD_COMPANY = (
    "User has no access to add a team as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY = (
    "Given '%s' is already exists, so choose another",
    "COMPANY_NAME_ALREADY_EXISTS"
)
INVALID_USER_IDS_FOR_ADD_COMPANY = (
    "Given users '%s' are invalid(not found), please check it",
    "INVALID_USER_IDS"
)

DUPLICATE_USER_IDS_FOR_ADD_COMPANY = (
    "Given users '%s' are duplicated, please check it",
    "DUPLICATE_USER_IDS"
)

USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY = (
    "User has no access to delete company details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_COMPANY_ID_FOR_DELETE_COMPANY = (
    "Given company id is invalid(NotFound)",
    "INVALID_COMPANY_ID"
)

USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY = (
    "User has no access to update company details as he is not an admin",
    "USER_HAS_NO_ACCESS"
)

INVALID_COMPANY_ID_FOR_UPDATE_COMPANY = (
    "Given company id is invalid(NotFound)",
    "INVALID_COMPANY_ID"
)

COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY = (
    "Given '%s' name is already exists, so updating name is not possible.",
    "COMPANY_NAME_ALREADY_EXISTS"
)

DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY = (
    "Given users '%s' are duplicated, so update is not possible",
    "DUPLICATE_USER_IDS"
)

INVALID_USER_IDS_FOR_UPDATE_COMPANY = (
    "Given users '%s' invalid(not found), so update is not possible",
    "INVALID_USER_IDS"
)

INVALID_NEW_PASSWORD = (
    "Given new password is not valid",
    "INVALID_NEW_PASSWORD"
)

INVALID_CURRENT_PASSWORD = (
    "Given current password is not valid",
    "INVALID_CURRENT_PASSWORD"
)
CURRENT_PASSWORD_MISMATCH = (
    "Given current password is not matching with the current password",
    "CURRENT_PASSWORD_MISMATCH"
)

INVALID_PROJECT_ID = (
    "Given project is not found",
    "INVALID_PROJECT_ID"
)

PROJECT_NAME_ALREADY_EXISTS = (
    "Given project name already exists, choose another",
    "PROJECT_NAME_ALREADY_EXISTS"
)

PROJECT_DISPLAY_ID_ALREADY_EXISTS = (
    "Given project display id already exists, choose another",
    "PROJECT_DISPLAY_ID_ALREADY_EXISTS"
)

USER_HAS_NO_ACCESS_TO_ADD_PROJECT = (
    "User has no access to add project",
    "USER_HAS_NO_ACCESS"
)

DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT = (
    "Duplicate roles has been given",
    "DUPLICATE_ROLE_IDS"
)

DUPLICATE_ROLE_NAMES = (
    "Duplicate role names has been given",
    "DUPLICATE_ROLE_NAMES"
)

ROLE_NAMES_ALREADY_EXISTS = (
    "Role names {role_names} already exist",
    "ROLE_NAMES_ALREADY_EXISTS"
)

USER_HAS_NO_ACCESS_TO_GET_PROJECTS = (
    "User has no access to get projects",
    "USER_HAS_NO_ACCESS_TO_GET_PROJECTS"
)

USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES = (
    "User has no access to get users with roles",
    "USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES"
)
