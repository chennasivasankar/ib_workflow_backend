

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8d9e745e-6725-4ae0-8a0e-15baf9781257",
    "team_ids": [
        "88e11d6d-56e8-4dab-af25-9cb342f19687"
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

