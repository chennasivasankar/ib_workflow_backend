from typing import Dict, Any, List

actions = [
    {
        "stage_id": "stage_1",
        "stage_display_logic": "logic_1",
        "action_name": "action_name_1",
        "role": "ROLE_!",
        "button_text": "button_text_1",
        "button_color": "button_color_1"
    }
]


def populate_stage_actions(actions: List[Dict]):
    actions_dto = []
    for action_dict in actions:
        validation_for_action_dict(action_dict)
        actions_dto.append(append_action_dict(action_dict))
    return actions_dto


def append_action_dict(action_dict: Dict[str, Any]):
    from ib_tasks.interactors.dtos import ActionDto
    return ActionDto(
        stage_id=action_dict['stage_id'],
        action_name=action_dict['action_name'],
        logic=action_dict['stage_display_logic'],
        role=action_dict['role'],
        button_text=action_dict['button_text'],
        button_color=action_dict.get("button_color")
    )


def validation_for_action_dict(action_dict: Dict[str, Any]):
    if not action_dict.get("stage_id"):
        raise_exception_for_valid_format()
        return
    if not action_dict.get("stage_display_logic"):
        raise_exception_for_valid_format()
        return
    if not action_dict.get("action_name"):
        raise_exception_for_valid_format()
        return
    if not action_dict.get("role"):
        raise_exception_for_valid_format()
        return
    if not action_dict.get("button_text"):
        raise_exception_for_valid_format()
        return
    if not action_dict.get("button_color"):
        raise_exception_for_valid_format()
        return


class InvalidFormatException(Exception):
    def __init__(self, valid_format: str):
        self.valid_format = valid_format


def raise_exception_for_valid_format():
    valid_format = {
        "stage_id": "stage_1",
        "stage_display_logic": "logic_1",
        "action_name": "action_name_1",
        "roles": "ROLE_!",
        "button_text": "button_text_1",
        "button_color": "button_color_1"
    }
    import json
    json_valid_format = json.dumps(valid_format)
    raise InvalidFormatException(valid_format=json_valid_format)
