

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "530d5870-82f6-431b-9b37-cae8f02d681a",
    "team_ids": [
        "82c56c22-e148-4652-a786-201548dd3356"
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

