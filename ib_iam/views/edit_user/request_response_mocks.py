

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "dc1a1c36-8b95-4180-a3c8-f2092c6fe5d5",
    "team_ids": [
        "39434e1c-7723-4515-8fce-f57b51cc0e9e"
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

