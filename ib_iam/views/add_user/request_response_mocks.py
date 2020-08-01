

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "99a6a288-8e83-4566-966a-cf7ee8395a01",
    "team_ids": [
        "5db61899-d475-470d-a66c-9f4a66412b59"
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

