

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e3b8b12f-df7c-4ac3-8a26-b8a923c8b65f",
    "team_ids": [
        "b6ca8f01-ca3a-4a96-92be-ad1c4c96ff4f"
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

