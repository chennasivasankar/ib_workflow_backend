

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "93e02e31-49e3-489c-9921-3f858f946333",
    "team_ids": [
        "ead31991-2b45-476e-92bd-a843ef4bd28e"
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

