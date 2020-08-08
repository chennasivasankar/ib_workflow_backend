

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fcd98b21-a179-401d-bc3e-985820fbd1b1",
    "team_ids": [
        "45d0d1b6-a164-44f4-b20c-73fbc6e5cbc5"
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

