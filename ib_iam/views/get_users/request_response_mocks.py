


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "2bed304c-b42f-4422-bac5-59e41926fed7",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "c4936a0f-ad68-49bd-9be5-71d3e0813f2b",
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
                "company_id": "dc917932-9f4b-4425-9f04-021e59316fb1",
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

