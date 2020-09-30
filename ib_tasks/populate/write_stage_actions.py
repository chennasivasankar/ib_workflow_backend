from ib_tasks.interactors.stages_dtos import StageActionLogicDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionIdFunctionPathDTO


def writing_data_to_stage_actions_logic():
    from yapf.yapflib.yapf_api import FormatCode
    from ib_tasks.storages.action_storage_implementation \
        import ActionsStorageImplementation
    from django.conf import settings
    storage = ActionsStorageImplementation()
    actions_dto = storage.get_database_stage_actions()
    file_path_name = 'ib_tasks/populate/stage_actions_logic_{}.py'.format(
        settings.STAGE)
    with open(file_path_name, "w") as file_:
        content = ''
        for action_dto in actions_dto:
            content += _define_single_method(action_dto=action_dto)
            action_dto.py_function_import_path = file_path_name
        formatted_content = FormatCode(content)[0]
        file_.write(formatted_content)
        file_.close()
    change_action_dtos = [
        ActionIdFunctionPathDTO(
            action_id=action_dto.action_id,
            py_function_import_path=action_dto.py_function_import_path
        )
        for action_dto in actions_dto
    ]
    storage.update_stage_actions_func_path(change_action_dtos)


def _define_single_method(action_dto: StageActionLogicDTO):
    stage_id = action_dto.stage_id
    action_name = action_dto.action_name
    action_logic = action_dto.action_logic
    function_as_str = ''
    function_name = f'{stage_id}_{action_name}'
    function_name = function_name.replace(' ', '_').replace('-', '_').replace(
        '\n', '')
    function_as_str += f"\n\ndef {function_name}(task_dict, global_constants, stage_value_dict):\n"

    action_logic_lines = action_logic.split("\n")
    new_lines = []
    for line in action_logic_lines:
        line = '\t' + line
        new_lines.append(line)

    new_action_logic = "\n".join(new_lines)
    function_as_str += new_action_logic + "\n"
    function_as_str += "\t" + "return task_dict\n"
    return function_as_str
