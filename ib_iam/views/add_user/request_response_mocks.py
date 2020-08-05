

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2677ec28-d75c-427c-b92d-b8af6708f2c5",
    "team_ids": [
        "607c178e-62a4-4fb2-9287-a74fe1a4104f"
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

