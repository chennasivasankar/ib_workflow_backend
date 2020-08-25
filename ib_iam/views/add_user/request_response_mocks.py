

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ebfb8f60-ae3b-416e-a642-1735acf03b96",
    "team_ids": [
        "b962f180-ffdd-486d-92bb-5a834b883999"
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

