

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "2d6929f2-a91b-4697-a9b1-0fe37d2e3422",
    "team_ids": [
        "8ac61f68-0a05-4364-a9e9-a97e4726dc31"
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

