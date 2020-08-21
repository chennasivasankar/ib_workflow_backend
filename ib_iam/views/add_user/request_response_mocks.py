

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5c89c1e4-a766-491b-84a6-0199bda027bd",
    "team_ids": [
        "707bde6d-c654-4d4e-beef-8ecef6444840"
    ],
    "role_ids": [
        "string"
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

