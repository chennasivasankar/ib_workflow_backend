

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "065011bc-2a0c-4abe-81a2-d278e7bb9dca",
    "team_ids": [
        "8753e946-b3be-405f-a30c-6a59c16a6bd3"
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

