

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "506d6374-3aaa-4c74-b250-10d445e5cddf",
    "team_ids": [
        "d875a00d-4171-4574-a769-622812d0a016"
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

