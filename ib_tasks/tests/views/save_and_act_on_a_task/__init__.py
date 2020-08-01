# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "save_and_act_on_a_task"
REQUEST_METHOD = "post"
URL_SUFFIX = "task/save_and_act/v1/"

from .test_case_01 import TestCase01SaveAndActOnATaskAPITestCase

__all__ = [
    "TestCase01SaveAndActOnATaskAPITestCase"
]
