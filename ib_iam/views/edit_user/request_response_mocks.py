

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3256fe16-dacd-4e14-907d-5dbc14720f41",
    "team_ids": [
        "de04ff7d-3555-4f98-8c05-e47d9d6b27a8"
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

