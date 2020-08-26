

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "6da52561-2a1c-4312-89b6-b409ce3fb6d4",
    "team_ids": [
        "63d960d3-6f79-4f8b-bfd0-4925d366c5a1"
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

