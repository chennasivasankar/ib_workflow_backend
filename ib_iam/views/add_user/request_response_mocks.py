

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "75250fc3-4d36-4bab-83be-28ec14d1a9db",
    "team_ids": [
        "cb9519e2-c475-4518-a494-391b53f98e8f"
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

