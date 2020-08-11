

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4c978d37-674d-49a0-a671-a8dd05a12c0e",
    "team_ids": [
        "a34a895b-4ead-4a6c-b166-f9908125cf1a"
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

