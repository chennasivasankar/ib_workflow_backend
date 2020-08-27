

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3e0a6958-507b-45e2-96a7-c695e4f1f5b9",
    "team_ids": [
        "0e424784-9bbe-4a41-a347-66b664fc6d8f"
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

