

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "140932cc-51b9-48c8-a63f-3895ced76dcc",
    "team_ids": [
        "a0c0b89f-4d0d-4567-9c78-cd5657485d79"
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

