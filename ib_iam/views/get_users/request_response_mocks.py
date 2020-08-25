


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9c219fc4-d324-4887-b845-83ecf5df7181",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b5845890-c591-409a-88a7-81c5d1baca17",
                    "team_name": "string"
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

