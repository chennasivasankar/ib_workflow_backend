

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e63fa9e2-27af-4dfa-8ef7-dc1faa216d61",
    "team_ids": [
        "623d59ae-8a0c-48f7-bef8-dcfba550b5db"
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

