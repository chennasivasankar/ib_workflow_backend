

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "893d9312-129b-4abd-9cd6-ab00fa11aa83",
    "team_ids": [
        "283599df-d2ae-4c9c-9c14-a09369b613de"
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

