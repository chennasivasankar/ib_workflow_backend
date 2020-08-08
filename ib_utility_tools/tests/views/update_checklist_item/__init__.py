# pylint: disable=wrong-import-position

APP_NAME = "ib_utility_tools"
OPERATION_NAME = "update_checklist_item"
REQUEST_METHOD = "put"
URL_SUFFIX = "checklist/item/{checklist_item_id}/v1/"

from .test_case_01 import TestCase01UpdateChecklistItemAPITestCase

__all__ = [
    "TestCase01UpdateChecklistItemAPITestCase"
]
