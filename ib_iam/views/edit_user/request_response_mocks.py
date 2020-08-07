

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3df1048c-2d08-4e85-b85c-fbddb5cd6a87",
    "team_ids": [
        "7a458646-8ced-4958-a927-f5a9564e3069"
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

