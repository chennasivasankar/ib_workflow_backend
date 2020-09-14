

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "68cbf2c1-ac4f-473a-b927-dde2ddaea4fa",
    "team_ids": [
        "299e0d5b-02ab-4042-a13b-3e047bc847dd"
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

