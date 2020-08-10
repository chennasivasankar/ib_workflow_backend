

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9cb8d0e7-eec4-4c2f-9531-78c249f06c59",
    "team_ids": [
        "13669709-6a99-4fc0-ab0a-938b50b49d61"
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

