

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "cb7ef423-3a4a-42f6-9345-c009cc2331d8",
    "team_ids": [
        "7182ad8c-01dd-4743-9cdd-e082d9b19c0f"
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

