

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fc803dba-8aab-4933-8ddb-920bd70a7e8d",
    "team_ids": [
        "bcec72f7-c37f-4c7d-9986-2fa09fd0f533"
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

