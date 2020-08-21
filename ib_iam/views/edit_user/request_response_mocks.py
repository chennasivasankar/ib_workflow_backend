

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d61962b4-6c0c-406d-b181-5d8b733c600f",
    "team_ids": [
        "9f664198-9a4b-4010-8261-2fc5c5103ee9"
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

