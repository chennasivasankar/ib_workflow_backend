

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a5727778-42e6-4bb8-9aed-cc5a014bfbd4",
    "team_ids": [
        "97f2c92a-5680-4c1c-8400-56365ae480c9"
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

