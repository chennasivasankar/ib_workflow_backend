

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f403d079-c03c-4c1d-9be3-44d41effefa1",
    "team_ids": [
        "77ab11da-6fda-4c59-9ce6-eaddff0e4d95"
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

