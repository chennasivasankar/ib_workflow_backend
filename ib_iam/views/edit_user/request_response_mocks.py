

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8ddde445-7e63-4059-9fd2-fce1b3fce465",
    "team_ids": [
        "120e7c5b-4b67-4fee-bfd7-eaab4b5dc762"
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

