

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "7e17e059-c8de-471f-ab0b-211e42f7030b",
    "team_ids": [
        "ad7b938b-e70c-4e12-84c1-62a835703744"
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

