

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fdcc0ce9-d658-4f66-bf08-548f3546a8c7",
    "team_ids": [
        "d90ead98-e2d0-4614-a7c3-a84e0451c7bc"
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

