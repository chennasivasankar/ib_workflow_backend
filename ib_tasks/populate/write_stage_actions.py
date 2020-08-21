from ib_tasks.interactors.stages_dtos import StageActionLogicDTO


def writing_data_to_stage_actions_logic():
    from ib_tasks.storages.action_storage_implementation \
        import ActionsStorageImplementation
    storage = ActionsStorageImplementation()
    actions_dto = storage.get_database_stage_actions()

    with open('ib_tasks/populate/stage_actions_logic.py', "a") as file:
        for action_dto in actions_dto:
            _define_single_method(file=file, action_dto=action_dto)
        file.close()


def _define_single_method(file, action_dto: StageActionLogicDTO):
    stage_id = action_dto.stage_id
    action_name = action_dto.action_name
    action_logic = action_dto.action_logic
    function_name = f'{stage_id}_{action_name}'
    function_name = function_name.replace(' ', '_').replace('-', '_').replace(
        '\n', '')
    file.write(
        f"\n\ndef {function_name}(task_dict, global_constants, stage_value_dict):\n")

    action_logic_lines = action_logic.split("\n")
    new_lines = []
    for line in action_logic_lines:
        line = '\t' + line
        new_lines.append(line)

    new_action_logic = "\n".join(new_lines)
    file.write(new_action_logic + "\n")
    file.write("\t" + "return task_dict\n")