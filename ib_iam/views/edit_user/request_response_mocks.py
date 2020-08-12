

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a30a540c-79ad-4e41-bf83-961f38db261b",
    "team_ids": [
        "a5b4cc74-a93c-400d-8e0f-551f7371e27a"
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

