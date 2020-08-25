

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9c5833de-3c3a-41dc-802c-678e5210239b",
    "team_ids": [
        "2299a4b9-22a4-4efb-98af-f27f9c6157d6"
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

