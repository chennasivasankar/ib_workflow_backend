from typing import Dict, Any, List


def populate_stage_flows(stage_flow_dicts: List[Dict]):
    validation_for_stage_flow_dict(stage_flow_dicts)
    stage_flows_dtos = [
        append_action_dict(action_dict)
        for action_dict in stage_flow_dicts
    ]
    from ib_tasks.interactors.create_stage_flow_interactor import CreateStageFlowInteractor
    from ib_tasks.storages.storage_implementation import StagesStorageImplementation
    from ib_tasks.storages.action_storage_implementation import ActionsStorageImplementation
    stage_storage = StagesStorageImplementation()
    action_storage = ActionsStorageImplementation()
    interactor = CreateStageFlowInteractor(
        stage_storage=stage_storage, action_storage=action_storage
    )
    interactor.create_stage_flows(stage_flow_dtos=stage_flows_dtos)


def append_action_dict(stage_dict: Dict[str, Any]):
    previous_stage_id = stage_dict['previous_stage_id'].strip('\n')
    action_name = stage_dict['action_name'].strip('\n')
    next_stage_id = stage_dict['next_stage_id'].strip('\n')
    from ib_tasks.interactors.storage_interfaces.stage_dtos import CreateStageFlowDTO
    return CreateStageFlowDTO(
        previous_stage_id=previous_stage_id,
        action_name=action_name,
        next_stage_id=next_stage_id
    )


def validation_for_stage_flow_dict(stage_flow_dicts: List[Dict]):
    from schema import Schema, SchemaError
    from schema import And
    schema = Schema(
        [{
            "previous_stage_id": And(str, len),
            "action_name": And(str, len),
            "next_stage_id": And(str, len)
        }],
        ignore_extra_keys=True
    )
    try:
        schema.validate(stage_flow_dicts)
    except SchemaError:
        raise_exception_for_valid_format()


def raise_exception_for_valid_format():
    valid_format = {
        "previous_stage_id": "stage_1",
        "action_name": "Submit",
        "next_stage_id": "stage_2"
    }
    import json
    json_valid_format = json.dumps(valid_format)
    from ib_tasks.exceptions.custom_exceptions \
        import InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
