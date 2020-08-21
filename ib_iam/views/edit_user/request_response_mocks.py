

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "678263a4-6171-4f53-8087-6012764ab0e6",
    "team_ids": [
        "b54f409a-701d-4db8-a57a-75e11ef1c200"
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

