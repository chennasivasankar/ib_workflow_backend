

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "logo_url": "string",
    "team_ids": [
        "string"
    ],
    "project_display_id": "string",
    "roles": [
        {
            "role_name": "string",
            "description": "string"
        }
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "PROJECT_NAME_ALREADY_EXISTS"
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
    "res_status": "INVALID_TEAM_IDS"
}
"""

