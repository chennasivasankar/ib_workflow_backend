

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "user_ids": [
        "string"
    ]
}
"""


RESPONSE_201_JSON = """
{
    "team_id": "f773c632-f949-4f08-9b2f-f80cac9c9e22"
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
    "res_status": "INVALID_USERS"
}
"""

