

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b8beb30c-340f-40a2-9676-0d9651938890",
    "team_ids": [
        "b03cad4f-3c16-41da-93df-8691fd90ed66"
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

