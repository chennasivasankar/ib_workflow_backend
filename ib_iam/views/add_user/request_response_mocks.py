

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5f9f67c7-77fe-4624-aeed-f78b189c3162",
    "team_ids": [
        "8129fbfa-5cd7-4c75-97c5-04b8ffcfc207"
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

