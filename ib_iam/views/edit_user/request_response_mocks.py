

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f5038486-a9c5-4377-ab4c-b0f63585bce6",
    "team_ids": [
        "10f444f8-4f4f-4b3b-9367-ec2da9e8a229"
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

