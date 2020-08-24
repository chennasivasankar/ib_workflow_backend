

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "27f456f7-4ab5-43ab-b0dc-abd10e287bea",
    "team_ids": [
        "1b3fa820-85eb-4d40-be6d-d982bee8a71b"
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

