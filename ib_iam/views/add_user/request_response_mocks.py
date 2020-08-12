

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c7713f8b-38b0-4ca5-b977-fea937406e13",
    "team_ids": [
        "95ca6124-2078-4033-acb6-963249f8adca"
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

