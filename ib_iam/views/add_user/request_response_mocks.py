

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "384c2889-43fc-40ac-9eb9-b0e302c522ee",
    "team_ids": [
        "68fea3f9-e5c9-4330-a54c-67906a8d87b7"
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

