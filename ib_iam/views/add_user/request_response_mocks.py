

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "589107c6-e34b-4668-91a2-a314f7c98a2e",
    "team_ids": [
        "fe771110-328b-4e36-af60-f19dc510ba36"
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

