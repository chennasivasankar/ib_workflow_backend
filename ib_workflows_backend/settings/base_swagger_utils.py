from ib_workflows_backend.settings.base import *

# swagger utils #

PRINT_REQUEST_RESPONSE_TO_CONSOLE = False

STORE_LATENCY_OBJECT = True

INSERT_LAST_ACCESS_REQUIRED = True

STORE_LAST_ACCESS_OBJECT = True

DSU_RAISE_EXCEPTION_FOR_API_RESPONSE_STATUS_CODE = True  # default value is False, if this setting not present

################ Installed Apps ###############

# Application definition
from django_swagger_utils.drf_server.utils.general.import_app_settings import \
    import_app_settings

THIRD_PARTY_APPS = [
    "ib_users"
]
APPS = [
    "ib_iam",
    "ib_tasks",
    "ib_boards",
    "ib_discussions",
    "ib_utility_tools",
    "ib_adhoc_tasks"
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += APPS

THIRD_PARTY_SWAGGER_APPS = [
    # insert your apps here, in this order third part apps specific settings will be loaded.
    "ib_sentry_wrapper",
    "s3_uploader"
]
INSTALLED_APPS += THIRD_PARTY_SWAGGER_APPS

# this will import all settings from [APPS].conf.settings
for app_name in THIRD_PARTY_SWAGGER_APPS + APPS:
    try:
        _dict = import_app_settings(app_name)
        locals().update(
            {name: _dict["module_dict"][name] for name in _dict["to_import"]})
    except ImportError as err:
        print(err)

# *************************** Swagger Utils ***************************

from django_swagger_utils.drf_server.utils.decorator.getDecryptedData import \
    getDecryptedData
from django_swagger_utils.drf_server.utils.decorator.getPrivateKeyFromClientKeyRelatedDetails import \
    getPrivateKeyFromClientKeyRelatedDetails

SWAGGER_UTILS = {
    "DEFAULTS": {
        "REQUEST_WRAPPING_REQUIRED": False,
        "REQUEST_ENCRYPTION_REQUIRED": False,
        "GET_CLIENT_KEY_DETAILS_FUNCTION": getPrivateKeyFromClientKeyRelatedDetails,
        "GET_DECRYPTED_DATA_FUNCTION": getDecryptedData,
        "RESPONSE_SERIALIZER_VALIDATION": True
    },
    "CUSTOM_EXCEPTIONS": {
        "CustomException": {
            "http_status_code": 404,
            "is_json": True,
        }
    },
    "APPS": {
        "ib_iam": {"dsu_version": "1.0"},
        "ib_tasks": {"dsu_version": "1.0"},
        "ib_boards": {"dsu_version": "1.0"},
        "ib_discussions": {"dsu_version": "1.0"},
        "ib_utility_tools": {"dsu_version": "1.0"},
        "ib_adhoc_tasks": {"dsu_version": "1.0"}

    },
    "HOST": os.environ.get('APIGATEWAY_ENDPOINT', '127.0.0.1:8000'),
}

API_KEY_AUTHENTICATION_CLASS = \
    "ib_workflows_backend.common.authentication.APIKeyAuthentication"

CUSTOM_EXCEPTIONS_TO_LOG_IN_SENTRY = []

AUTH_USER_MODEL = "ib_users.UserAccount"

DEFAULT_OAUTH_APPLICATION_NAME = os.environ.get(
    "DEFAULT_OAUTH_APPLICATION_NAME", "")
DEFAULT_OAUTH_CLIENT_ID = os.environ.get("DEFAULT_OAUTH_CLIENT_ID", "")
DEFAULT_OAUTH_CLIENT_SECRET = os.environ.get("DEFAULT_OAUTH_CLIENT_SECRET", "")
DEFAULT_OAUTH_SCOPES = os.environ.get("DEFAULT_OAUTH_SCOPES",
                                      "read write update delete")
DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS = int(
    os.environ.get("DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS", "100000000"))

# ****************** S3 Uploader Config ******************
S3_COGNITO_POOL_REGION_NAME = os.environ.get("S3_COGNITO_POOL_REGION_NAME")
S3_COGNITO_IDENTITY_POOL_ID = os.environ.get("S3_COGNITO_IDENTITY_POOL_ID")
S3_COGNITO_DEVELOPER_IDENTITY_NAME = os.environ.get(
    "S3_COGNITO_DEVELOPER_IDENTITY_NAME")

S3_UPLOADER_FOLDER_PREFIX = "uploads"
S3_UPLOADER_OBJECT_ACL = "public-read"
S3_UPLOADER_URL_TYPE = "cloudfront"

# ****************** ElasticSearch Config ******************
ELASTICSEARCH_ENDPOINT = os.environ.get(
    'ELASTICSEARCH_ENDPOINT', 'localhost:9200'
)
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': ELASTICSEARCH_ENDPOINT
    },
}

# *********************  Authentication **************
RESET_PASSWORD_LINK_EXPIRY_IN_SECONDS = \
    int(os.environ.get("RESET_PASSWORD_LINK_EXPIRY_IN_SECONDS", '3600'))

USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS = \
    int(os.environ.get("USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS", '3600'))

FRONTEND_URL = os.environ.get(
    "FRONTEND_URL",
    'https://ib-workflows-web-alpha.apigateway.in/'
)

RESET_PASSWORD_LINK = '{frontend_url}update-password?token='.format(
    frontend_url=FRONTEND_URL
)

USER_VERIFICATION_EMAIL_LINK = "{frontend_url}verify-email?token=".format(
    frontend_url=FRONTEND_URL
)

JGC_DRIVE_PROJECT_ID = os.environ.get(
    "JGC_DRIVE_PROJECT_ID", "JGC_DRIVE_PROJECT_ID"
)

JGC_DEFAULT_ROLE = os.environ.get(
    "JGC_DEFAULT_ROLE", "JGC_USER"
)

# StageFlow URLs
CCBP_COMPLETE_WORKFLOW_LINK = os.environ.get(
    "CCBP_COMPLETE_WORKFLOW_LINK", "https://onthegomodel.com/ccbp"
)
CCBP_USER_WORKFLOW_LINK = os.environ.get(
    "CCBP_USER_WORKFLOW_LINK", "https://onthegomodel.com/ccbp"
)
