

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8aeb5879-700e-4b1c-900c-5c5cdaadda7a",
    "team_ids": [
        "c568d8ec-d8af-4e7d-9c29-aa767d3a2e89"
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

