

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8467ee09-32c1-4970-b961-8401eae105dc",
    "team_ids": [
        "f84dab9d-8b5c-47ea-9e1d-12f252b21afd"
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

