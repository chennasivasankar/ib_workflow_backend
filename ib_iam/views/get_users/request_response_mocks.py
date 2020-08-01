


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "02d52366-4c8e-4ac3-b485-e43ad6280a51",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6b445533-0538-4be1-8b6f-7dfdd31e700a",
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
                "company_id": "413038ff-266b-419a-b1cb-978969316dba",
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

