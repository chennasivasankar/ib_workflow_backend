

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "780c1f6d-b631-4712-a175-1f0e09101613",
    "team_ids": [
        "f3f5a19a-ed13-48a1-b711-39278fd8d9c2"
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

