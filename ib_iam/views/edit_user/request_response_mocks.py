

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "197925cb-9c3d-4600-a388-5fd278833383",
    "team_ids": [
        "ce5d1d41-dff3-4a60-94f2-1bb68bc36417"
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

