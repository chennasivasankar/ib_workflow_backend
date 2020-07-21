# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "delete_team"
REQUEST_METHOD = "delete"
URL_SUFFIX = "team/{team_id}/v1/"

from .test_case_01 import TestCase01DeleteTeamAPITestCase
from .test_case_02 import TestCase02DeleteTeamAPITestCase
from .test_case_03 import TestCase03DeleteTeamAPITestCase

__all__ = [
    "TestCase01DeleteTeamAPITestCase",
    "TestCase02DeleteTeamAPITestCase",
    "TestCase03DeleteTeamAPITestCase"
]
