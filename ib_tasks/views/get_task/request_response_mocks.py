


RESPONSE_200_JSON = """
{
    "task_id": "string",
    "template_id": "string",
    "gofs": [
        {
            "gof_id": "string",
            "gof_fields": [
                {
                    "field_id": "string",
                    "field_response_single_value": "string",
                    "field_response_multiple_values": [
                        "string"
                    ],
                    "is_readable": true,
                    "is_writable": true
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

