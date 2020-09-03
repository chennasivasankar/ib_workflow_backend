

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f840e84d-c8d8-4332-a2cf-12e450d4ee1d",
    "team_ids": [
        "20f240d8-f60f-4cc9-ba70-1603b4dc4c23"
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

