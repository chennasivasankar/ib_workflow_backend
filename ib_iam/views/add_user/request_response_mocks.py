

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "24c5d656-ffaa-403a-b980-ebd21283cfd2",
    "team_ids": [
        "97c9423e-b820-493a-8fc8-4e4ff0221bd5"
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

