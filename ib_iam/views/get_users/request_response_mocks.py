


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "32dd90e0-e14f-484f-8498-23704a7dae16",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b9688e3d-dad4-4b78-8109-a788b26eb58e",
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

