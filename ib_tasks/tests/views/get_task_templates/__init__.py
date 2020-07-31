# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_task_templates"
REQUEST_METHOD = "get"
URL_SUFFIX = "task_templates/v1/"

from .test_case_01 import TestCase01GetTaskTemplatesAPITestCase
from .test_case_02 import TestCase02GetTaskTemplatesAPITestCase

__all__ = [
    "TestCase01GetTaskTemplatesAPITestCase",
    "TestCase02GetTaskTemplatesAPITestCase"
]
