

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9b05772a-eac6-4e06-a5e3-d1ebf1bf69bc",
    "team_ids": [
        "5ede68d8-6475-456c-8072-383b89bc5102"
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

