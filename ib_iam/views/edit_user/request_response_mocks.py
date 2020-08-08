

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4bc5951e-cc08-4405-9a11-6d302b4e33dd",
    "team_ids": [
        "7d6a7b26-2d55-49f6-a465-e6a0d8c06b78"
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

