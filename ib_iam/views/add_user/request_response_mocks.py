

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "97d11a8e-554d-4ad7-877d-a6506d19c611",
    "team_ids": [
        "939ec1d2-241c-42fb-a2b9-91cce1549c0a"
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

