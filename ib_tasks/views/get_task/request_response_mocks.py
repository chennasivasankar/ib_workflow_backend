


RESPONSE_200_JSON = """
{
    "task_id": 1,
    "template_id": "string",
    "gofs": [
        {
            "gof_id": "string",
            "same_gof_order": 1.1,
            "gof_fields": [
                {
                    "field_id": "string",
                    "field_response": "string"
                }
            ]
        }
    ],
    "stages_with_actions": [
        {
            "stage_id": "string",
            "stage_display_name": "string",
            "actions": [
                {
                    "action_id": "string",
                    "button_text": "string",
                    "button_color": "string"
                }
            ]
        }
    ]
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

