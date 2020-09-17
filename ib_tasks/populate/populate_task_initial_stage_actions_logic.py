from typing import Dict, Any, List

from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation


def populate_tasks(tasks: List[Dict]):
    tasks_dto = []
    validation_for_tasks_dict(tasks)
    tasks = _remove_white_spaces_and_apply_replaces_to_roles(
        tasks)
    for action_dict in tasks:
        tasks_dto.append(append_action_dict(action_dict))
    from ib_tasks.interactors.configure_initial_task_template_stage_actions \
        import ConfigureInitialTaskTemplateStageActions

    from ib_tasks.storages.action_storage_implementation import \
        ActionsStorageImplementation
    interactor = ConfigureInitialTaskTemplateStageActions(
        storage=ActionsStorageImplementation(),
        tasks_dto=tasks_dto,
        template_storage=TaskTemplateStorageImplementation()
    )
    interactor.create_update_delete_stage_actions_to_task_template()


def _remove_white_spaces_and_apply_replaces_to_roles(
        action_dicts: List[Dict]):
    for action_dict in action_dicts:
        roles = action_dict['roles']
        roles = roles.replace(" ", "")
        roles = roles.split("\n")
        action_dict["roles"] = roles
    return action_dicts


def append_action_dict(action_dict: Dict[str, Any]):
    stage_id = action_dict["stage_id"]
    function_path = 'ib_tasks.populate.stage_actions_logic.'
    action_name = action_dict["action_name"]
    function_name = f'{stage_id}_{action_name}'
    function_name = function_name.replace(' ', '_').replace('-', '_').replace(
        '\n', '')
    function_path = function_path + function_name
    from ib_tasks.interactors.stages_dtos import TaskTemplateStageActionDTO
    return TaskTemplateStageActionDTO(
        task_template_id=action_dict['task_template_id'].strip('\n'),
        stage_id=action_dict['stage_id'].strip('\n'),
        action_name=action_dict['action_name'],
        logic=action_dict['action_logic'],
        roles=action_dict['roles'],
        function_path=function_path,
        button_text=action_dict['button_text'],
        button_color=action_dict.get("button_color"),
        action_type=action_dict['action_type'],
        transition_template_id=action_dict['transition_template_id']
    )


def validation_for_tasks_dict(tasks_dict: List[Dict]):
    from schema import Schema, Optional, SchemaError
    schema = Schema(
        [{
            "task_template_id": str,
            "stage_id": str,
            "action_logic": str,
            "action_name": str,
            "roles": str,
            "button_text": str,
            Optional("button_color"): str,
            "action_type": str,
            "transition_template_id": str
        }],
        ignore_extra_keys=True
    )

    try:
        validated_data = schema.validate(tasks_dict)
    except SchemaError:
        raise_exception_for_valid_format()
        return
    for action_dict in validated_data:
        _validate_action_logic(action_logic=action_dict['action_logic'])


def _validate_action_logic(action_logic: str):
    from astroid import parse, AstroidSyntaxError
    from ib_tasks.exceptions.custom_exceptions \
        import InvalidPythonCodeException
    try:
        parse(action_logic)
    except AstroidSyntaxError:
        raise InvalidPythonCodeException()


def raise_exception_for_valid_format():
    valid_format = {
        "task_template_id": "task_template_1",
        "stage_id": "stage_1",
        "action_logic": "logic_1",
        "action_name": "action_name_1",
        "roles": "ROLE_1",
        "button_text": "button_text_1",
        "button_color": "button_color_1",
        "action_type": "NO VALIDATIONS",
        "transition_template_id": "transition_id"
    }
    import json
    json_valid_format = json.dumps(valid_format)
    from ib_tasks.exceptions.custom_exceptions \
        import InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
