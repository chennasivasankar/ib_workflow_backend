

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c704d635-5ded-4c79-8481-675dd57e2d19",
    "team_ids": [
        "9b3c8752-2311-4776-9e34-85e4372a6fd8"
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

