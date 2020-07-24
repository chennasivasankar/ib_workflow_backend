

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "35f84226-2a18-40ec-864a-547e9bd5b844",
    "team_ids": [
        "16fb927a-c359-42b2-9a0a-15bcb881d637"
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

