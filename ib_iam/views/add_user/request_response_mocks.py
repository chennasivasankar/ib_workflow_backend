

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d1cf046c-6ba3-47d2-807c-de722de04640",
    "team_ids": [
        "03154125-fdf3-49cc-911e-ac5c7b4fd30c"
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

