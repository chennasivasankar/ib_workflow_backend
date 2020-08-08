

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2e857b74-eb58-4309-bd8a-f3834dd6bfcb",
    "team_ids": [
        "d8053cac-f052-4d24-a739-45a08e60611a"
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

