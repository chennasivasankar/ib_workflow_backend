# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_team_details"
REQUEST_METHOD = "put"
URL_SUFFIX = "team/{team_id}/"

from .test_case_01 import TestCase01UpdateTeamDetailsAPITestCase

__all__ = [
    "TestCase01UpdateTeamDetailsAPITestCase"
]
