

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "36e3cd86-7e31-4042-bb1c-7bad063bbbbc",
    "team_ids": [
        "54e33dc0-200c-491d-bf8e-e5d933f26f43"
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

