

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fb9a28f9-8018-4283-a9f0-0d6869eee202",
    "team_ids": [
        "a68ca6e8-3cd5-45da-a673-0b0ed2c27490"
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

