

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9c10f946-15b2-42ef-b03d-f72bf20479ee",
    "team_ids": [
        "1ac1d1c1-496a-4132-a4f3-b8bac2ecc5cb"
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

