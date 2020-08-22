

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a9bd25b2-5005-445d-921b-5c412e506765",
    "team_ids": [
        "7de64870-3400-4280-be90-2f0508eb1b4a"
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

