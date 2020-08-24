

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3c0aa054-4d2b-4d9e-ba3e-f80a356dc36e",
    "team_ids": [
        "f7b7caa7-1504-4391-bc77-13a188e23d1b"
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

