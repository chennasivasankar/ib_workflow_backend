

REQUEST_BODY_JSON = """
{
    "filter_id": 1,
    "action": "ENABLED"
}
"""


RESPONSE_200_JSON = """
{
    "filter_id": 1,
    "action": "ENABLED"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_FILTER_ID"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DO_NOT_HAVE_PERMISSION_TO_FILTER"
}
"""

