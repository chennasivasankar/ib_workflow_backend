

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2270fd75-b422-4651-8f91-6addb414b7d9",
    "team_ids": [
        "01e512e1-24c6-46b7-bd54-540637b574da"
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

