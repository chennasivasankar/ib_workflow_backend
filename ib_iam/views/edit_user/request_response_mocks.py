

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "05c0304f-8021-4f08-8bc0-395cbd7ebf0d",
    "team_ids": [
        "6884d9f4-110d-4d10-b084-fe24d557a953"
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

