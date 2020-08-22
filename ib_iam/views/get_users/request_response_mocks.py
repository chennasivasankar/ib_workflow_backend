


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b6810e0b-834e-46b9-aeef-fb89cc78c3c9",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "def9bccc-f1c0-4761-a3b3-0920b4805f92",
                    "team_name": "string"
                }
            ],
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "company": {
                "company_id": "string",
                "company_name": "string"
            }
        }
    ],
    "total": 1
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_LIMIT"
}
"""

