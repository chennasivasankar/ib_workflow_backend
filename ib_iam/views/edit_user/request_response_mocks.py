

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "94d93695-1a99-4aa0-9fb9-305fba3bdc84",
    "team_ids": [
        "57e8aa58-33f1-4bfd-95e0-a43a54593d43"
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

