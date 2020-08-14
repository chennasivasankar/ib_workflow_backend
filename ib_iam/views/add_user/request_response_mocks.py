

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a5928cfe-dded-4c53-8609-db0cefed0e3e",
    "team_ids": [
        "81dbb9a4-f7ee-4baf-aea5-b699560fb50c"
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

