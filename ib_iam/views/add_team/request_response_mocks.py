

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string"
}
"""


RESPONSE_201_JSON = """
{
    "team_id": "string"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DUPLICATE_TEAM_NAME"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS"
}
"""

