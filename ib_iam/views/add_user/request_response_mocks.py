

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5acd471f-d09e-42e8-a508-a99308566437",
    "team_ids": [
        "6ab27840-2f90-45f0-b1c5-76a80ab9d3dc"
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

