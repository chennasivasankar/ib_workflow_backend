

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "859edc6a-059d-4b9e-9010-bf3b1a41ce8d",
    "team_ids": [
        "c68f0440-3619-4654-9223-ff536968d39c"
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

