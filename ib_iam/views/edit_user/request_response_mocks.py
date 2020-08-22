

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4cf8b756-4bd6-4c13-845c-cfb740ae1775",
    "team_ids": [
        "5abd50fe-c461-4593-8ee6-9df2fb4ddf7c"
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

