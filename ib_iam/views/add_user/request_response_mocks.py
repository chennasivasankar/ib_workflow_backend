

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c43208d0-f68a-4dfc-8839-07f82c7a345f",
    "team_ids": [
        "87cb3131-49e2-4991-ade1-641177f3cf5d"
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

