

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0dbac626-b7e9-486c-bed3-27ce87bee71e",
    "team_ids": [
        "a0cb7cb9-1f5a-4d31-9acb-bc23ad18af60"
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

