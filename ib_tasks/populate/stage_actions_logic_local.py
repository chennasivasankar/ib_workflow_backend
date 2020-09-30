def IN_PROGRESS_To_Do(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "TO_DO"
    return task_dict


def IN_PROGRESS_To_Be_Reviewed(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "TO_BE_REVIEWED"
    return task_dict


def TO_BE_REVIEWED_In_Progress(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "IN_PROGRESS"
    return task_dict


def TO_BE_REVIEWED_Review_Rejected(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "REVIEW_REJECTED"
    return task_dict


def TO_BE_REVIEWED_Done(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "DONE"
    return task_dict


def TO_BE_REVIEWED_To_Do(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "TO_DO"
    return task_dict


def REVIEW_REJECTED_To_Do(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "TO_DO"
    return task_dict


def TO_DO_In_Progress(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "IN_PROGRESS"
    return task_dict


def CREATE_STAGE_Create_Task(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "TO_DO"
    return task_dict


def JGC_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_DRAFTS"
    return task_dict


def JGC_DRAFTS_Make_Call_1(task_dict, global_constants, stage_value_dict):
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


def JGC_CALL2_ATTEMPTED_Have_more_queries(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_ESCALATED_TO_CENTRAL_TEAM"
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


def JGC_CALL2_REATTEMPT_Have_more_queries(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_ESCALATED_TO_CENTRAL_TEAM"
    return task_dict


def JGC_CALL2_REATTEMPT_Interested_in_course(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_REGISTRATION_PENDING_Registration_Complete(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_SUCCESSFUL_LEAD"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Decision_Pending(task_dict, global_constants,
                                               stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_FOLLOWUP_CALL"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Interested_in_course(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_REGISTRATION_PENDING"
    return task_dict


def JGC_EXPLORING_FREE_ACCESS_Have_more_queries(task_dict, global_constants,
                                                stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_ESCALATED_TO_CENTRAL_TEAM"
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


def JGC_FOLLOWUP_CALL_Have_more_queries(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_ESCALATED_TO_CENTRAL_TEAM"
    return task_dict


def JGC_FOLLOWUP_CALL_Not_interested(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_LEAD_LOST"
    return task_dict


def JGC_FOLLOWUP_CALL_Registration_complete(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_SUCCESSFUL_LEAD"
    return task_dict


def JGC_CREATE_LEAD_Save_as_Draft(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_DRAFTS"
    return task_dict


def JGC_CREATE_LEAD_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "JGC_CALL1_ATTEMPTED"
    return task_dict
