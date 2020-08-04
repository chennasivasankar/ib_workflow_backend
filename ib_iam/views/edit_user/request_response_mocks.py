

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a74b0637-e87d-4f96-b0dc-7a3fabbfc992",
    "team_ids": [
        "0b67d4ec-caf2-4305-9cd3-30d9acc6e66a"
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

