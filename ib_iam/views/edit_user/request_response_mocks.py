

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c2b8e56c-e884-4744-b2c0-0f3b49df6fef",
    "team_ids": [
        "42342590-6373-44e0-ad0b-4348c1844073"
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

