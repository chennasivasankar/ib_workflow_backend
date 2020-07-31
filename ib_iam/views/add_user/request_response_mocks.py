

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "275b7c69-9113-4ac2-a51a-a057b2e28de9",
    "team_ids": [
        "b4ff93c5-1a79-4bdf-9bdb-71c5d45fc934"
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

