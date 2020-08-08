# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_transition_template"
REQUEST_METHOD = "get"
URL_SUFFIX = "transition_template/{transition_template_id}/v1/"

from .test_case_01 import TestCase01GetTransitionTemplateAPITestCase
from .test_case_02 import TestCase02GetTransitionTemplateAPITestCase

__all__ = [
    "TestCase01GetTransitionTemplateAPITestCase",
    "TestCase02GetTransitionTemplateAPITestCase"
]
