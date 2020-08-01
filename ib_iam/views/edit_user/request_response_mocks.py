

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "dcde9d4c-1c86-46e7-80f5-a4fb6c2aa5f2",
    "team_ids": [
        "e146eb3c-aa24-4220-b947-4393b79e1774"
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

