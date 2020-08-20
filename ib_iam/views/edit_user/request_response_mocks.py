

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "6f3624e0-e12e-411f-8072-5e2fb8920040",
    "team_ids": [
        "7c4b70e1-6a25-4c5b-a873-a5d93b121de8"
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

