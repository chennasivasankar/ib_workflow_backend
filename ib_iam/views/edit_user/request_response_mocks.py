

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "907ec067-3571-4681-9ef3-3bb0c3c0b856",
    "team_ids": [
        "f01bb150-10f2-4244-b0ba-5187995e327f"
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

