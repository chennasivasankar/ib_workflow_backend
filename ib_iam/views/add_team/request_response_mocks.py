

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "member_ids": [
        "string"
    ]
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
    "res_status": "TEAM_NAME_ALREADY_EXISTS"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_MEMBERS"
}
"""

