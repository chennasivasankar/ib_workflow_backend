# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_list_of_teams"
REQUEST_METHOD = "get"
URL_SUFFIX = "teams/"

from .test_case_01 import TestCase01GetListOfTeamsAPITestCase

__all__ = [
    "TestCase01GetListOfTeamsAPITestCase",
]
