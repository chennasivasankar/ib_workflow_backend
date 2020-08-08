

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "27a4c838-f7c3-497c-8888-634473f2dea1",
    "team_ids": [
        "90fc6354-dae1-45ba-bf4c-61dbf4647cc5"
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

