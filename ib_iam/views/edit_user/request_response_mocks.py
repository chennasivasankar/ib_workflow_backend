

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9da7dccb-1578-47bf-aa42-0c38968b84e6",
    "team_ids": [
        "c0f5a619-e5a1-41c3-96b7-00f7e62581a4"
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

