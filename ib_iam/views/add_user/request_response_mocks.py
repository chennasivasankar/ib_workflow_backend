

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f3f22f51-e605-4df3-958e-2d0f5223c028",
    "team_ids": [
        "79b9caa8-d30c-42a6-966b-4171546f332f"
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

