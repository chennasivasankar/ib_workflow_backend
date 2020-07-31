

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0d66bd1e-edf7-460b-aa65-3c51062859ab",
    "team_ids": [
        "eb68315a-09e2-4394-b233-96d926d05008"
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

