

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3d1b1393-c3b5-4acc-a9c1-7aadb80ea2e2",
    "team_ids": [
        "12b6b0f5-492a-4bc8-8a11-27fb4f9a1d59"
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

