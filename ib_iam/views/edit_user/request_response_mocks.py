

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "559adb54-85a1-49c2-ad0e-c89b302da01a",
    "team_ids": [
        "d0c6b920-a666-4e88-9426-52756f619a93"
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

