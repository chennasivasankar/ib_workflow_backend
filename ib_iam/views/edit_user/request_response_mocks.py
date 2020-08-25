

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d97b646b-a72d-44bb-87cc-2f6326c80f76",
    "team_ids": [
        "a8255231-f47b-447c-903a-4ea4c167b947"
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

