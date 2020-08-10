

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b36ae715-1d13-4c23-a04d-1f3ee0367069",
    "team_ids": [
        "50bf8e9e-4fd5-41b5-b174-b78d7b78aa95"
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

