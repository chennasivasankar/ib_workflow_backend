# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_transition_template"
REQUEST_METHOD = "get"
URL_SUFFIX = "transition_template/{transition_template_id}/v1/"

from .test_case_01 import TestCase01GetTransitionTemplateAPITestCase
from .test_case_02 import TestCase02GetTransitionTemplateAPITestCase
from .test_case_03 import TestCase03GetTransitionTemplateAPITestCase
from .test_case_04 import TestCase04GetTransitionTemplateAPITestCase
from .test_case_05 import TestCase05GetTransitionTemplateAPITestCase
from .test_case_06 import TestCase06GetTransitionTemplateAPITestCase
from .test_case_07 import TestCase07GetTransitionTemplateAPITestCase
from .test_case_08 import TestCase08GetTransitionTemplateAPITestCase

__all__ = [
    "TestCase01GetTransitionTemplateAPITestCase",
    "TestCase02GetTransitionTemplateAPITestCase",
    "TestCase03GetTransitionTemplateAPITestCase",
    "TestCase04GetTransitionTemplateAPITestCase",
    "TestCase05GetTransitionTemplateAPITestCase",
    "TestCase06GetTransitionTemplateAPITestCase",
    "TestCase07GetTransitionTemplateAPITestCase",
    "TestCase08GetTransitionTemplateAPITestCase"
]
