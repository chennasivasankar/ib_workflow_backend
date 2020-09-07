


RESPONSE_200_JSON = """
{
    "stages": [
        {
            "stage_id": 1,
            "name": "string",
            "color": "string"
        }
    ],
    "actions": [
        {
            "previous_stage": 1,
            "action_name": "string",
            "next_stage": 1
        }
    ]
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TEMPLATE_ID"
}
"""

