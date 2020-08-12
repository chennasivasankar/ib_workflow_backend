

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8371ea40-4d1e-4a84-8d05-ecce062b8992",
    "team_ids": [
        "e3b18048-1cfb-4f0b-bef8-bbc44d74b985"
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

