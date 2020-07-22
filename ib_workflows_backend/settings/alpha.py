from ib_workflows_backend.settings.base_server import *

from .db_logging import *

from .base_server import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "TRUE") == "TRUE"

ALLOWED_HOSTS += [
    "ib-workflows-backend-alpha.apigateway.in"
]
