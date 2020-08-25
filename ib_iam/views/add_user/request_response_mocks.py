

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fc825ab1-7bfe-4892-9188-197f1b18ced7",
    "team_ids": [
        "7e7e4f06-092c-4c2c-a9c6-121e83a3eb19"
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

