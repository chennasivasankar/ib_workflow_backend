

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "657e845e-df15-452f-bede-e63d5f167218",
    "team_ids": [
        "6973f19e-17a8-41ee-994a-bf3df42515b4"
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

