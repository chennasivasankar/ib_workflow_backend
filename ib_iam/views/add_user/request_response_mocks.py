

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "52cf8a96-96ec-476a-b6d3-884b5b3d7693",
    "team_ids": [
        "f134f1bf-4a08-4099-b2dd-0a3f2df2f18e"
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

