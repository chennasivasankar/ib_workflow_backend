

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "84dcfeb4-688b-4b8c-b31b-296233df4519",
    "team_ids": [
        "0ff6479e-4f4a-48ce-936f-463d53ba3893"
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

