

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c92b5681-53fc-4a2a-b8ca-573c30f0d28f",
    "team_ids": [
        "bdf6ef04-6602-484f-8f3d-d114ee7908f8"
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

