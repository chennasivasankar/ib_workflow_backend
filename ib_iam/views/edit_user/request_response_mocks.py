

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d7097817-5c4a-418f-9b9c-23d542d76d68",
    "team_ids": [
        "7d372e47-3f46-42ef-8cb1-69625795a1fc"
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

