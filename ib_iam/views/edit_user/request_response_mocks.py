

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ce00af86-cc68-4e09-b27f-f53d3baf348d",
    "team_ids": [
        "f79a6e93-fe50-4f66-8342-03b250d4d61b"
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

