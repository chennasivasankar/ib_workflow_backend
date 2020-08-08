

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "34888335-1d6d-4030-811c-eba2680ae305",
    "team_ids": [
        "568ed323-ccdf-408e-8453-3708e35bdba3"
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

