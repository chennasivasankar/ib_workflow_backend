

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c5281d28-c8b1-4bff-bffc-f98bc88edd1f",
    "team_ids": [
        "c6b74822-0550-4c3a-bf6f-9db4c6d8c478"
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

