

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "94d45f2b-dcde-4eee-8cc8-0bd4de2e6329",
    "team_ids": [
        "1aac19dc-f896-4e57-9d9c-88ee03e6326b"
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

