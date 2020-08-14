

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "94b0c807-9583-4b09-bc29-f144edb9b4e8",
    "team_ids": [
        "0d1eeb22-aa4c-4c0a-8726-d957b9619377"
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

