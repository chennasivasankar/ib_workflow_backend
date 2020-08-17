

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3bac1f93-cd04-4c06-ba46-1f5602fe8c2c",
    "team_ids": [
        "e31bcbac-d842-416b-a642-6e7531ddfb15"
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

