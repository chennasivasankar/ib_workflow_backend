

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9221f50f-0491-449d-9db0-8ae3b7c20747",
    "team_ids": [
        "351f32a2-5ab4-499b-a167-76a4dd4d4ab8"
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

