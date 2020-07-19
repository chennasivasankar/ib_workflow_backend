# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_team"
REQUEST_METHOD = "post"
URL_SUFFIX = "team/add/v1/"

from .test_case_01 import TestCase01AddTeamAPITestCase
from .test_case_02 import TestCase02AddTeamAPITestCase
from .test_case_03 import TestCase03AddTeamAPITestCase

__all__ = [
    "TestCase01AddTeamAPITestCase",
    "TestCase02AddTeamAPITestCase",
    "TestCase03AddTeamAPITestCase"
]
