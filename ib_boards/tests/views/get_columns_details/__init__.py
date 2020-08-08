# pylint: disable=wrong-import-position

APP_NAME = "ib_boards"
OPERATION_NAME = "get_columns_details"
REQUEST_METHOD = "post"
URL_SUFFIX = "boards/{board_id}/columns/v1/"

from .test_case_01 import TestCase01GetColumnsDetailsAPITestCase

__all__ = [
    "TestCase01GetColumnsDetailsAPITestCase"
]
