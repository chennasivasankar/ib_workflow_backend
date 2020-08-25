

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
    "team_ids": [
        "89d96f4b-c19d-4e69-8eae-e818f3123b09"
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

