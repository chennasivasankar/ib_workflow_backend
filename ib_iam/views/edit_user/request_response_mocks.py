

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "0466f1ef-8674-417b-a3bb-c1d4bb3bd50b",
    "team_ids": [
        "22637469-318d-4eb2-becc-f00f8fe907c4"
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

