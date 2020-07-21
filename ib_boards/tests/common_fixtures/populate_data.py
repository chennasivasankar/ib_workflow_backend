"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""


def populate_dict_with_invalid_keys():
    data = [
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_1",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 1,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],
                    
                }
            """,
            "kanban_view_fields": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],
                    
                }
            """,
            "list_view_fields": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],
                    
                }
            """
        },
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_2",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 2,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    }
                """,
            "kanban_view_fields": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    }
                """,
            "list_view_fields": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    }
                """
        }
    ]
    return data


def populate_dict_with_invalid_json():
    data = [
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_1",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 1,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                }
            """,
            "kanban_view_fields": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                }
            """,
            "list_view_fields": """
                {
                    "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                    "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                }
            """
        },
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_2",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 2,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    },
                """,
            "kanban_view_fields": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    }
                """,
            "list_view_fields": """
                    {
                        "FIN_PR":[PR_PAYMENT_REQUEST_DRAFTS, PR_PENDING_RP_APPROVAL],
                        "FIN_IN":[PR_NEED_CLARIFICATION, PR_APPROVED],

                    }
                """
        }
    ]
    return data


def populate_dict_with_valid_data():
    import json
    json_object = """
                {
                    "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS", "PR_PENDING_RP_APPROVAL"],
                    "FIN_IN": ["PR_NEED_CLARIFICATION", "PR_APPROVED"]

                }
            """
    data = [
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_1",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 1,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": json_object,
            "kanban_view_fields": json_object,
            "list_view_fields": json_object,
        },
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_2",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 2,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": json_object,
            "kanban_view_fields": json_object,
            "list_view_fields": json_object
        }
    ]
    return data


def populate_dict_with_invalid_json_for_summary_fields():
    import json
    json_object = """
                {
                    "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS", "PR_PENDING_RP_APPROVAL"],
                    "FIN_IN": ["PR_NEED_CLARIFICATION", "PR_APPROVED"]

                }
            """
    data = [
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_1",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 1,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": json_object,
            "kanban_view_fields": """
                {
                    "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS", "PR_PENDING_RP_APPROVAL"],
                    "FIN_IN": ["PR_NEED_CLARIFICATION", "PR_APPROVED"]

                },
            """,
            "list_view_fields": json_object,
        },
        {
            "board_id": "BOARD_ID_1",
            "board_display_name": "BOARD_DISPLAY_NAME",
            "column_id": "COLUMN_ID_2",
            "column_display_name": "COLUMN_DISPLAY_NAME",
            "display_order": 2,
            "user_role_ids": ['USER', 'ADMIN'],
            "column_summary": "COLUMN_SUMMARY",
            "column_actions": 'COLUMN_ACTIONS',
            "task_template_stages": json_object,
            "kanban_view_fields": json_object,
            "list_view_fields": json_object
        }
    ]
    return data