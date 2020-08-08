# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_task_templates_fields_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "task_templates_fields/v1/"

from .test_case_01 import TestCase01GetTaskTemplatesFieldsDetailsAPITestCase

__all__ = [
    "TestCase01GetTaskTemplatesFieldsDetailsAPITestCase"
]
