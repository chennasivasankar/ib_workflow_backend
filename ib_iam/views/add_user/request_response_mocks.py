

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c634ad64-f8a5-421c-a037-d1b7c07d3f7c",
    "team_ids": [
        "33a0508e-fd9a-4655-99a1-079877b3cfb8"
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

