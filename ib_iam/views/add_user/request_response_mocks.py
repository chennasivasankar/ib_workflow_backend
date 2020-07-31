

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "628c1f50-465d-48f7-bc42-a4c6b1959cc2",
    "team_ids": [
        "2d0dbc78-49a3-42b4-8e47-f8e478fb7242"
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

