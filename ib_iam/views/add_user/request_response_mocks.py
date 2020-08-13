

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "205f3dc5-d0bb-4808-9226-ba2a78c4080d",
    "team_ids": [
        "985a7cde-49bd-43a5-a929-42319db24fb4"
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

