

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "129166bf-9a8a-4f5c-8ad4-9f9cb1a9cb1a",
    "team_ids": [
        "fe834407-cf47-4833-8b9d-92a174a590f2"
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

