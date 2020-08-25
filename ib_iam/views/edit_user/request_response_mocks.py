

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "995595de-9ae2-423e-baa3-bce3aa6fc0ec",
    "team_ids": [
        "75497a76-6594-4703-885e-4d6f5f82b825"
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

