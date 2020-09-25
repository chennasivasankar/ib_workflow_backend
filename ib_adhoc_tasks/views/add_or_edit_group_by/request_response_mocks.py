

REQUEST_BODY_JSON = """
{
    "view_type": "LIST",
    "group_by_key": "string",
    "order": 1,
    "group_by_id": 1
}
"""


RESPONSE_200_JSON = """
{
    "group_by_id": 1,
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

