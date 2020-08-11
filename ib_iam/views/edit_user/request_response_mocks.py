

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f669508c-b4b5-42ce-9e4e-2ef0828b689c",
    "team_ids": [
        "398658dd-6c3a-4d11-9291-8d1cef6b7c5c"
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

