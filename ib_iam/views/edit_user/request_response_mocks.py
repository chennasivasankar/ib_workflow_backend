

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fea724c8-224e-4abe-b450-4e483f858d78",
    "team_ids": [
        "12fd43df-694e-4756-82a1-5897aec4dea5"
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

