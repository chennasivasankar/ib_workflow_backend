

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "bf810a01-f2db-4bfd-9d32-451e312dc9c1",
    "team_ids": [
        "1fe35f67-585c-4c5d-a342-228d46821f3a"
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

