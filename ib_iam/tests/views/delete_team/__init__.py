# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "delete_team"
REQUEST_METHOD = "delete"
URL_SUFFIX = "team/{team_id}/"

from .test_case_01 import TestCase01DeleteTeamAPITestCase

__all__ = [
    "TestCase01DeleteTeamAPITestCase"
]
