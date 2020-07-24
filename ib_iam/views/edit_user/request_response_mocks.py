

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "33c9cdfe-3e63-4321-a6ed-2343e0be73c8",
    "team_ids": [
        "d0389535-bf13-4e5d-8cf2-698d20bfb9cf"
    ],
    "role_ids": [
        "string"
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_EMAIL"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_COMPANY_ID"
}
"""

