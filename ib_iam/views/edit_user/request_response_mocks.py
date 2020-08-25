

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "93b8f82d-bac8-44e0-b293-62e9eebcab15",
    "team_ids": [
        "db4c5dd8-c6be-4338-9004-69a3adc86296"
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

