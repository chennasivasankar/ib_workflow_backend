

def stage_1_action_name_1(task_dict, global_constants,
                          stage_value_dict):
    task_dict['random_gof']['random_key'] = "sample_text"

    return task_dict


def stage_1_action_name_2(task_dict, global_constants,
                          stage_value_dict):
    denominator = task_dict['gof1']['field1']
    value = 56/denominator

    return task_dict


def stage_1_action_name_3(task_dict, global_constants,
                          stage_value_dict):
    task_dict['status_variables']['variable_1'] = 'stage_2'

    return task_dict