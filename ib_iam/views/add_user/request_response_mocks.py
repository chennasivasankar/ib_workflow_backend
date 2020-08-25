

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "79dab726-50a5-451c-9b63-969fe4f33989",
    "team_ids": [
        "7fe305a9-8c59-4240-8da5-5f2b4ae28975"
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

