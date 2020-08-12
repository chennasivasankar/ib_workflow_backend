

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "7b1ae527-e86a-48fc-86ec-17cd61dc8f5f",
    "team_ids": [
        "945c1493-ad73-4902-93c4-fa50cadd7877"
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

