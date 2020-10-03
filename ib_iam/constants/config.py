REQUIRED_PASSWORD_MIN_LENGTH = '8'
REQUIRED_PASSWORD_SPECIAL_CHARS = '`~!@#$%^&*()+-_[]{}|;:",.<>/?'
ALL_ROLES_ID = "ALL_ROLES"
MINIMUM_USER_NAME_LENGTH = 5
EMAIL_DOMAIN_VALIDATION_EXPRESSION = "\@(.*?)\."

VALID_EMAIL_DOMAINS = ["ibhubs", "proyuga", "cybereye", "gmail"]
PASSWORD_VALIDATION_EXPRESSION = \
    r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$"
ROLES_SUBSHEET_NAME = "Roles"
PROJECT_SUBSHEET_NAME = "Projects"
PROJECT_ID_PREFIX = "project_{}"
ROLE_ID_PREFIX = "role_{}"
EMAIL_VALIDATION_PATTERN = "(^[a-zA-Z]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]+$)"

DEFAULT_PASSWORD = "Password123#"

DEFAULT_TEAM_ID = 'b8cb1520-279a-44bb-95bf-bbca3aa057ba'
DEFAULT_TEAM_NAME = "DEFAULT_TEAM_NAME"

DEFAULT_CONFIGURATION_TEAM_ID = 'a7db1520-279a-44bb-95bf-bbca3aa057ba'
DEFAULT_CONFIGURATION_TEAM_NAME = 'DEFAULT_CONFIGURATION_TEAM_NAME'

LEVEL_0_NAME = "level_0"
LEVEL_1_NAME = "level_1"
LEVEL_2_NAME = "level_2"

LEVEL_0_HIERARCHY = 0
LEVEL_1_HIERARCHY = 1
LEVEL_2_HIERARCHY = 2
# if we add a new project add every config key even it is false
PROJECTS_CONFIG = {
    "JGC_DRIVE": {
        "restrict_assignee_to_user": True,
        "enable_adhoc_template": False
    }
}
PROJECT_DEFAULT_PREFIX = "IBWF"
