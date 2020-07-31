

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4b89a248-2846-4faf-b948-d586b3f82b93",
    "team_ids": [
        "e06e62a4-db42-4142-8798-04fa51a1653d"
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

