

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f2a028c3-d532-47d3-97a1-f00624b3c353",
    "team_ids": [
        "e9fee8ff-de02-4295-8f11-fa06d1f52e24"
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

