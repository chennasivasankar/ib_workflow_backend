

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9085789e-6da7-485b-b68a-bcf9f1614cc3",
    "team_ids": [
        "c02bdbbb-7891-4ebe-af35-4287524075fc"
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

