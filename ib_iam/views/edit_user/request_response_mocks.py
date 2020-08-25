

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a67d3e88-772b-4413-8147-babf5fb40fac",
    "team_ids": [
        "e22c3dec-9b82-4f8c-90da-805ed9238772"
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

