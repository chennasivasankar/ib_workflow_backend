

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2fb1f8a9-2bd2-4071-b7ec-f8047cbde8e7",
    "team_ids": [
        "ee962b3c-2738-4f24-8814-e12a61f737be"
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

