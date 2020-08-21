

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ec143c70-eef5-40c6-8ed1-1723bb45f8ab",
    "team_ids": [
        "bbd584f1-4161-4f4b-8992-3f4a1c198806"
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

