

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "74accb24-f3df-4335-9f6e-3b1e18b4561b",
    "team_ids": [
        "41fdc64f-9013-4f14-91a6-16d52dba2bba"
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

