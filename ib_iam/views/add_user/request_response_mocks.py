

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d4598e94-9901-461a-9b90-54d5c208fbd5",
    "team_ids": [
        "1106ee3c-dfa6-4a38-96f7-57fe19beb826"
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

