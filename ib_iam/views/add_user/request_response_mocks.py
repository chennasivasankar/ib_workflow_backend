

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e39054fa-7035-4887-8acb-7ecbe3c97a71",
    "team_ids": [
        "943410b6-284e-4f50-a81b-1b3b1ee186ff"
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

