# pylint: disable=wrong-import-position

APP_NAME = "ib_utility_tools"
OPERATION_NAME = "create_checklist_item"
REQUEST_METHOD = "post"
URL_SUFFIX = "checklist/item/create/v1/"

from .test_case_01 import TestCase01CreateChecklistItemAPITestCase

__all__ = [
    "TestCase01CreateChecklistItemAPITestCase"
]
