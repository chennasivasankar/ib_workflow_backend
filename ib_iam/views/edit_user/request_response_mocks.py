

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "41267306-9a13-4c3c-8972-bef5262aa103",
    "team_ids": [
        "8073f137-c143-4b49-9ca7-8a0f2597def5"
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

