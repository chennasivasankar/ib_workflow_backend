

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b7667919-cfe3-4e7e-a3f4-052c6becbafd",
    "team_ids": [
        "34d296b8-4911-45e0-8404-21aae7fe3aff"
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

