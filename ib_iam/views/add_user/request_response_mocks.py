

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "575de9fb-766e-484a-8bad-46d243bf47d8",
    "team_ids": [
        "e999211b-6633-42be-9e7f-28a20b542d48"
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

