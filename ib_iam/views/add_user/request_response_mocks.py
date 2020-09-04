

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8254b611-a58d-4e13-af32-e112cd0ea28c",
    "team_ids": [
        "e611be83-4349-4fe4-88da-4f5c7c4029ea"
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

