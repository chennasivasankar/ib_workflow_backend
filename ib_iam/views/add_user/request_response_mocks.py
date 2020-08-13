

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b39f4a6b-8bed-4200-9147-61b4877a6e4a",
    "team_ids": [
        "c694d6c5-f8a1-441a-a2b0-aff7a7fc7af8"
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

