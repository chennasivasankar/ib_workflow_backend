

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8afcce39-1bd8-44b3-ad54-ccd7a317822e",
    "team_ids": [
        "2aaafaed-6002-4879-875f-f5ae2d075e47"
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

