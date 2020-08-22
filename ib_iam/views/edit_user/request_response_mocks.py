

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "609ea92b-61a0-4fc7-83b5-385db9aa0cef",
    "team_ids": [
        "f9dd3c73-4b30-4163-b11a-a9af7465b5cd"
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

