

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f1c82803-b66c-4def-af98-5af8af18fcc1",
    "team_ids": [
        "be6f72fd-4cb9-4ec4-a05f-405a0bf11400"
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

