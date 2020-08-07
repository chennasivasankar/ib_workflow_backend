

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e196c198-bcf3-43ff-9d72-51dae055b58c",
    "team_ids": [
        "364d3e03-9f26-4dcc-9ad5-9f3ec718de44"
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

