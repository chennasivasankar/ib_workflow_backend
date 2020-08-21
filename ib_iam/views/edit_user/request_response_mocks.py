

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "37facaa8-7503-436d-81e1-e5c12b26ddc0",
    "team_ids": [
        "e827dc91-df93-4ef5-aaf5-2e1362b58f35"
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

