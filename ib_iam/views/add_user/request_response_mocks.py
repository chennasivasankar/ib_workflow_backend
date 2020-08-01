

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ab126b9b-ec49-42f0-a8b0-f0ba0104d3bb",
    "team_ids": [
        "5a848c5c-8811-4535-81a7-c38a9415cd01"
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

