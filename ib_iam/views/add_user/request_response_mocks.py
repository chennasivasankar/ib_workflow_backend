

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "84851cde-19c4-4c8c-8dcc-82f411325c18",
    "team_ids": [
        "d58f4880-aea5-44a7-8ecc-758df22cd1cb"
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

