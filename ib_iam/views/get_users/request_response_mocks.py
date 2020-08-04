


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "062efa8d-54de-420c-871c-951a69b9ce06",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "39fd1629-f310-4983-a927-b09f43034678",
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
                "company_id": "e1020576-46ec-4427-a24d-680703109fa9",
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

