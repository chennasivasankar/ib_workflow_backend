# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_team"
REQUEST_METHOD = "post"
URL_SUFFIX = "team/add/"

from .test_case_01 import TestCase01AddTeamAPITestCase

__all__ = [
    "TestCase01AddTeamAPITestCase"
]
