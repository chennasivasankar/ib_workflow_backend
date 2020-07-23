"""
# get column tasks when given column id is valid
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from ib_boards.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {"column_id": "ibgroup"},
        "query_params": {"Limit": 475, "Offset": 498},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetColumnTasksAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetColumnTasksAPITestCase, self
              ).setupUser(
            username=username, password=password
        )
        self.create_boards()

    def test_case(self):
        response = self.default_test_case()
        self.assert_match_snapshot(
            name="response",
            value=response)
