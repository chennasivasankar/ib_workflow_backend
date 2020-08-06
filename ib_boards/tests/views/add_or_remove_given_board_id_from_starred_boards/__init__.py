# pylint: disable=wrong-import-position


APP_NAME = "ib_boards"
OPERATION_NAME = "add_or_remove_given_board_id_from_starred_boards"
REQUEST_METHOD = "post"
URL_SUFFIX = "boards/{board_id}/star/v1/"

from .test_case_01 import TestCase01AddOrRemoveGivenBoardIdFromStarredBoardsAPITestCase
from .test_case_02 import TestCase02AddOrRemoveGivenBoardIdFromStarredBoardsAPITestCase

__all__ = [
    "TestCase01AddOrRemoveGivenBoardIdFromStarredBoardsAPITestCase",
    "TestCase02AddOrRemoveGivenBoardIdFromStarredBoardsAPITestCase"
]
