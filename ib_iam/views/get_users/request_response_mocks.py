


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "1bfdac8f-09c4-4571-a4e4-0029d7303764",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "87157c78-32fc-431b-8d1e-2b9052f7590e",
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
                "company_id": "46e79ccf-6c78-4c7c-8d7d-642339e87455",
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

