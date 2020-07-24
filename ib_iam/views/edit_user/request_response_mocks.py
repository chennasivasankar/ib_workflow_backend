

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "753630ef-4ed4-464d-9950-d839392fbbd5",
    "team_ids": [
        "778eab4e-e260-48f6-a9fc-26b1fe3deba5"
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

