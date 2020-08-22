


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "03b8af34-417c-4af6-b405-540886c1ab48",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bc3fbb19-af97-457d-9dbb-536ee7385fc5",
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

