

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9765b415-950d-42dc-89c8-b53fdbf685d2",
    "team_ids": [
        "1baef49f-66ed-4cf4-99bd-ea4e0dc53076"
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

