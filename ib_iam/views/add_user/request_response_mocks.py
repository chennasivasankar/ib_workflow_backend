

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "51ac4222-dd4f-4273-aba9-5a45c79cb8c1",
    "team_ids": [
        "974c6d9f-c296-4ca5-ace2-bdd6d261a765"
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

