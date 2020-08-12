

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e8377a3f-d869-44d3-b248-28d698007b91",
    "team_ids": [
        "4dae0abd-8d51-4dc6-9a70-7d6faefb3bae"
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

