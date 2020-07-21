# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_team_details"
REQUEST_METHOD = "put"
URL_SUFFIX = "team/{team_id}/"

from .test_case_01 import TestCase01UpdateTeamDetailsAPITestCase
from .test_case_02 import TestCase02UpdateTeamDetailsAPITestCase
from .test_case_03 import TestCase03UpdateTeamDetailsAPITestCase
from .test_case_04 import TestCase04UpdateTeamDetailsAPITestCase
from .test_case_05 import TestCase05UpdateTeamDetailsAPITestCase
from .test_case_06 import TestCase06UpdateTeamDetailsAPITestCase

__all__ = [
    "TestCase01UpdateTeamDetailsAPITestCase",
    "TestCase02UpdateTeamDetailsAPITestCase",
    "TestCase03UpdateTeamDetailsAPITestCase",
    "TestCase04UpdateTeamDetailsAPITestCase",
    "TestCase05UpdateTeamDetailsAPITestCase",
    "TestCase06UpdateTeamDetailsAPITestCase"
]
