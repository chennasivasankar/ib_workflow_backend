

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5781c140-753e-453a-bafc-c305eccbad82",
    "team_ids": [
        "037e0ba2-f462-428a-bd83-d67f9d26cecb"
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

