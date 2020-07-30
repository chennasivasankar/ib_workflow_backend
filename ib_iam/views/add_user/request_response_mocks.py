

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "045c3978-2cf8-4fbc-ad00-e85e3663a237",
    "team_ids": [
        "f4e0ad99-dac4-4f8d-b7c6-bea2145ade99"
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

