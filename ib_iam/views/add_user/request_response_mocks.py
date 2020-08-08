

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b66751cc-20a6-42db-8cd3-7ef83980acb0",
    "team_ids": [
        "85af578f-462f-4114-b44e-3da2859b0848"
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

