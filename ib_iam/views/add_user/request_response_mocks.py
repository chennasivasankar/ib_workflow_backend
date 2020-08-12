

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ddf9c859-5f42-45fc-bcbb-534acdab5630",
    "team_ids": [
        "55650ef7-0226-4abb-88c4-a10ff70d1266"
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

