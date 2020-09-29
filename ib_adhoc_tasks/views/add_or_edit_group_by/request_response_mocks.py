

REQUEST_BODY_JSON = """
{
    "group_by_key": "string"
}
"""


RESPONSE_200_JSON = """
{
    "group_by_key": "string",
    "display_name": "string",
    "order": 1
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_PROJECT_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS_FOR_GIVEN_FIELD"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW"
}
"""

