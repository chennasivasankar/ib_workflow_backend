

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "bdb1ebaf-d2ff-4834-b9a5-8e4bc1cdfb16",
    "team_ids": [
        "b73aab39-7861-4d79-90e7-8639b9ab3dd3"
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

