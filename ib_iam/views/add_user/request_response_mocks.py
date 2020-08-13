

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "33d8a53b-1fa4-495c-b398-3803304d28a8",
    "team_ids": [
        "aa6ff242-89b9-4261-b18d-b8be6c4f50b4"
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

