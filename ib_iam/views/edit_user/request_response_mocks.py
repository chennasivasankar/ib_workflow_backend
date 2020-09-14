

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3a205f48-db25-44b9-ad64-e6d1d0c78fb0",
    "team_ids": [
        "e4453610-214d-4241-a570-c7138f266361"
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

