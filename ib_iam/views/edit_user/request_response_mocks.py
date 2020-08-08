

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "09ba7e03-b337-4592-aa32-d3ae89a90628",
    "team_ids": [
        "bc729d8e-fea3-45f4-b35e-f7f25874b208"
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

