

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4b8b7da2-202e-4d4d-8ca9-fbca1834bf3f",
    "team_ids": [
        "612533c2-7ada-41ca-b9fb-3dfc4906e30e"
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

