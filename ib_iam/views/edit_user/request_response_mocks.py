

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e7568021-f987-4c5e-b952-a58ec0a9d97c",
    "team_ids": [
        "35df7a14-ad20-4002-a68e-ac67d515acb8"
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

