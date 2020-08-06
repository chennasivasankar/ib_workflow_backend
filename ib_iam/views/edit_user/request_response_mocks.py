

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ad5ead01-03c8-4ace-82e0-b088feedb909",
    "team_ids": [
        "ab2573ec-97a5-4631-8d62-abcb84a7a6ad"
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

