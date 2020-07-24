

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4bd9582d-92ab-49e9-914d-252195a823ec",
    "team_ids": [
        "8c1a8302-876f-41db-b9d7-c610f236ecb0"
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

