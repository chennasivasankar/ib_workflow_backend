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