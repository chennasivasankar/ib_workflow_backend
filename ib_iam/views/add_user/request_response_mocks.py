

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "1997123f-9036-4f1c-9a6d-5b7812ec6506",
    "team_ids": [
        "7b37ad93-c02e-49a4-8cf5-aeb895b5aa76"
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

