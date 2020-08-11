

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "fa47cdbf-3626-44da-9d14-399ebfa3b442",
    "team_ids": [
        "49e4982e-9576-4224-8c67-9a625e9df082"
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

