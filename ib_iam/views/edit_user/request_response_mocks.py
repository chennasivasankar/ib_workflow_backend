

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9f98cab5-3cb0-4a5a-b9b0-94ed7683870d",
    "team_ids": [
        "c6fc3095-e4b6-4dc9-8ee8-a1ae6e3b1518"
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

