

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2e071ccb-e8cf-4ad5-bbe7-327315651ac5",
    "team_ids": [
        "2b00c36a-99e5-429d-bfea-f13038b04404"
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

