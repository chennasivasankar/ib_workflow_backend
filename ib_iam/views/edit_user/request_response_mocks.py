

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a5a4760c-d6b1-472f-b893-37bccda1e526",
    "team_ids": [
        "c7e7f4ec-50d7-4dae-b946-ddde7036999e"
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

