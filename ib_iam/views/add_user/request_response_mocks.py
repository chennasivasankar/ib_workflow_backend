

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "1db3df64-4917-43b3-aa67-0de0a3c74a7e",
    "team_ids": [
        "b957d85d-c693-40cf-a593-083582e8bc1c"
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

