

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5ba04df2-d315-4686-a195-544ea3cc8835",
    "team_ids": [
        "6d0d292c-1ba9-4fb6-bc62-ae753f3212f7"
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

