# pylint: disable=wrong-import-position

APP_NAME = "ib_utility_tools"
OPERATION_NAME = "get_checklist"
REQUEST_METHOD = "post"
URL_SUFFIX = "checklist/v1/"

from .test_case_01 import TestCase01GetChecklistAPITestCase

__all__ = [
    "TestCase01GetChecklistAPITestCase"
]
