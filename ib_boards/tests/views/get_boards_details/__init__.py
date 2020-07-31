# pylint: disable=wrong-import-position

APP_NAME = "ib_boards"
OPERATION_NAME = "get_boards_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "boards/v1/"

from .test_case_01 import TestCase01GetBoardsDetailsAPITestCase

__all__ = [
    "TestCase01GetBoardsDetailsAPITestCase"
]
