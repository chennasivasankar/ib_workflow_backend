

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4a47e022-42bd-48b7-a62d-bcb3a7ecce6c",
    "team_ids": [
        "83b5210a-395d-4fa3-a358-78e0ddcd2444"
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

