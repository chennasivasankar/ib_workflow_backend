# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "create_transistion_checklist"
REQUEST_METHOD = "post"
URL_SUFFIX = "transition_checklist/v1/"

from .test_case_01 import TestCase01CreateTransistionChecklistAPITestCase

__all__ = [
    "TestCase01CreateTransistionChecklistAPITestCase"
]
