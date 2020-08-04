

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "639e7bb6-62f0-488c-9603-3e1dfb0abac7",
    "team_ids": [
        "4d6d18b1-b2f4-4e34-acde-62139ab1b042"
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

