

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5cb5146e-77bc-420a-9bd9-7b4d5e93bb6a",
    "team_ids": [
        "df3bc74e-a11f-46fb-9afa-16dcdb14abbe"
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

