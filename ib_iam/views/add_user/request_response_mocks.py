

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0884e9b5-0df0-4485-b93a-d30cf718a293",
    "team_ids": [
        "d6bf07f0-7a3c-4ed7-93b7-e204e37df437"
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

