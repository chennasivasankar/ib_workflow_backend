

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d5486d79-b58d-4983-8928-fb92bb337118",
    "team_ids": [
        "a049ba5f-2890-496e-9abb-9452a2433060"
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

