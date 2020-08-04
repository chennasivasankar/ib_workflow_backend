

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "32d90d38-1124-4af1-baa2-bf0f8e1f1108",
    "team_ids": [
        "cd0c38eb-a40c-4c62-8082-77d50c61ca6b"
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

