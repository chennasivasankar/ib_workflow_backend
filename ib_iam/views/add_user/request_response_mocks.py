

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "7e2cfb31-5148-4f9e-89fb-8b408e0b0e23",
    "team_ids": [
        "1835dcc1-0778-4055-9186-b6fa7dfc01d6"
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

