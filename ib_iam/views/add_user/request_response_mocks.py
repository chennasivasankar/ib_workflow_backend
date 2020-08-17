

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3e419169-012b-4e78-b076-8bb5deacf0de",
    "team_ids": [
        "9d4e2c95-df8e-4401-b0ad-9148c4e6b677"
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

