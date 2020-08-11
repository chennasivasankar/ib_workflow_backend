

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4fb692fa-ba65-4447-b8c3-8d4b5a2b9f81",
    "team_ids": [
        "ce8499c7-1ef1-4391-8a54-443f85f82393"
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

