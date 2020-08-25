

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a34e0a46-8802-43fe-9487-4c9fdefa1835",
    "team_ids": [
        "7174122f-fc66-4884-9d31-d92112f1ec68"
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

