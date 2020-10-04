def JGC_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_DRAFTS"
    return task_dict


def JGC_DRAFTS_Create_Lead(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEADS"
    return task_dict


def JGC_DRAFTS_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_ATTEMPTED"
    return task_dict


def JGC_LEADS_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_ATTEMPTED"
    return task_dict


def JGC_CALL1_ATTEMPTED_Not_answered(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_REATTEMPT"
    return task_dict


def JGC_CALL1_ATTEMPTED_Switched_off_or_Not_available(task_dict,
                                                      global_constants,
                                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_REATTEMPT"
    return task_dict


def JGC_CALL1_ATTEMPTED_Not_interested(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_CALL1_ATTEMPTED_Sent_Video(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_MAKE_CALL2"
    return task_dict


def JGC_CALL1_REATTEMPT_Not_answered(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_REATTEMPT"
    return task_dict


def JGC_CALL1_REATTEMPT_Switched_off_or_Not_available(task_dict,
                                                      global_constants,
                                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_REATTEMPT"
    return task_dict


def JGC_CALL1_REATTEMPT_Not_interested(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_CALL1_REATTEMPT_Sent_Video(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_MAKE_CALL2"
    return task_dict


def JGC_MAKE_CALL2_Make_Call_2(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL2_ATTEMPTED"
    return task_dict


def JGC_CALL2_ATTEMPTED_Not_answered(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL2_REATTEMPT"
    return task_dict


def JGC_CALL2_ATTEMPTED_Switched_off_or_Not_available(task_dict,
                                                      global_constants,
                                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL2_REATTEMPT"
    return task_dict


def JGC_CALL2_ATTEMPTED_Not_interested(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_CALL2_ATTEMPTED_Want_to_explore_more(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_EXPLORING_FREE_ACCESS"
    return task_dict


def JGC_CALL2_ATTEMPTED_Decision_Pending(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_FOLLOWUP_CALL"
    return task_dict


def JGC_CALL2_ATTEMPTED_Interested_in_course(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_CALL2_REATTEMPT_Not_answered(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL2_REATTEMPT"
    return task_dict


def JGC_CALL2_REATTEMPT_Switched_off_or_Not_available(task_dict,
                                                      global_constants,
                                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL2_REATTEMPT"
    return task_dict


def JGC_CALL2_REATTEMPT_Not_interested(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_CALL2_REATTEMPT_Want_to_explore_more(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_EXPLORING_FREE_ACCESS"
    return task_dict


def JGC_CALL2_REATTEMPT_Decision_Pending(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_FOLLOWUP_CALL"
    return task_dict


def JGC_CALL2_REATTEMPT_Interested_in_course(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_REGISTRATION_PENDING_Registration_Complete(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_SUCCESSFUL_LEAD"
    return task_dict


def JGC_REGISTRATION_PENDING_Not_Interested(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Decision_Pending(task_dict, global_constants,
                                               stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_FOLLOWUP_CALL"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Interested_in_course(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Not_interested(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Registration_complete(task_dict,
                                                    global_constants,
                                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_SUCCESSFUL_LEAD"
    return task_dict


def JGC_FOLLOWUP_CALL_Interested_in_course(task_dict, global_constants,
                                           stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_FOLLOWUP_CALL_Not_interested(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_FOLLOWUP_CALL_Registration_complete(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_SUCCESSFUL_LEAD"
    return task_dict


def JGC_LEAD_LOST_Interested_in_course(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_LEAD_LOST_Want_to_explore_more(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_EXPLORING_FREE_ACCESS"
    return task_dict


def JGC_LEAD_LOST_Generate_Link(task_dict, global_constants, stage_value_dict):
    import uuid

    task_dict["GOFID"][
        "FIELD_ID"] = "http://https://onthegomodel.com/{}".format(
            str(uuid.uuid4()))
    return task_dict


def JGC_CREATE_LEAD_Save_as_Draft(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_DRAFTS"
    return task_dict


def JGC_CREATE_LEAD_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_ATTEMPTED"
    return task_dict


def JGC_CREATE_LEAD_Create_Beneficiary(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEADS"
    return task_dict
