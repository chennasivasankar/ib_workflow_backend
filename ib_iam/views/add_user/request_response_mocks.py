

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f070e02a-4fdb-4e65-aff6-d428403e986b",
    "team_ids": [
        "baf41f82-eb3d-446c-8ee3-db53ac5a6b70"
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

