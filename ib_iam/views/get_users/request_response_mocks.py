


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "06f37f77-c5f9-4b72-a262-e8b51aa8c132",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8c3d9474-6245-42ef-b799-be96b3486ca3",
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
                "company_id": "41ee2a4c-4294-464f-8002-986b69471e06",
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

