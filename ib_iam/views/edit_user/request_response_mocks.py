

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "6ed2d6e4-3e0c-4d6d-b4a5-1267117f87c7",
    "team_ids": [
        "31b3b169-5cc8-47dd-8380-07d1bac217aa"
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

