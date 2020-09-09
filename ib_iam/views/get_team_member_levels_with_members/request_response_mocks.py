


RESPONSE_200_JSON = """
{
    "team_member_levels_with_members": [
        {
            "level_details": {
                "team_member_level_id": "097d3429-fc1e-43d5-83d5-8d691b895ae0",
                "team_member_level_name": "string",
                "level_hierarchy": 1
            },
            "level_members": [
                {
                    "member_id": "string",
                    "name": "string",
                    "profile_pic_url": "string",
                    "immediate_superior_team_user_id": "string",
                    "immediate_subordinate_team_members": [
                        {
                            "member_id": "string",
                            "name": "string",
                            "profile_pic_url": "string"
                        }
                    ]
                }
            ]
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TEAM_ID"
}
"""

