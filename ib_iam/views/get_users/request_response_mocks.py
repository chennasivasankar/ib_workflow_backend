


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "feac10e2-14d4-46ac-8979-736694bdd65b",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "0bfc727d-bee7-48a1-83c6-3c2ee4ff6465",
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
                "company_id": "d42d0d75-bc2c-4a85-8f88-a98e0856455a",
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

