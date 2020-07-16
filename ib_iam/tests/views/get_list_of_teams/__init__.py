# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_list_of_teams"
REQUEST_METHOD = "get"
URL_SUFFIX = "teams/"

from .test_case_01 import TestCase01GetListOfTeamsAPITestCase
from .test_case_02 import TestCase02GetListOfTeamsAPITestCase
from .test_case_03 import TestCase03GetListOfTeamsAPITestCase
from .test_case_04 import TestCase04GetListOfTeamsAPITestCase

__all__ = [
    "TestCase01GetListOfTeamsAPITestCase",
    "TestCase02GetListOfTeamsAPITestCase",
    "TestCase03GetListOfTeamsAPITestCase",
    "TestCase04GetListOfTeamsAPITestCase"
]
