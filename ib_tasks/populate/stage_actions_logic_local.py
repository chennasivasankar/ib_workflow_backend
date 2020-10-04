def CCBP_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_DRAFTS"
    return task_dict


def CCBP_DRAFTS_Create_Beneficiary(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEADS"

    if not task_dict.get("CCBP_SHAREABLE_LINKS", {}).get("CCBP_INVITE_CODE"):
        import uuid
        invite_code = str(uuid.uuid4())[:8]

        sharable_links_gof = task_dict.get("CCBP_SHAREABLE_LINKS", {})

        sharable_links_gof["CCBP_INVITE_CODE"] = invite_code

        sharable_links_gof[
            "CCBP_OTG_WEBSITE"] = "https://www.onthegomodel.com/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_FREE_ACCESS_PORTAL"] = "https://webinar.ibhubs.co/xpm-ccbp-limited-access-portal/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_CCBP_WEBSITE"] = "https://www.onthegomodel.com/ccbp/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_MORE_DETAILS_ABOUT_PROGRAM"] = "https://www.onthegomodel.com/ccbp/program-videos/?prospect={}".format(
            invite_code)

        task_dict["CCBP_SHAREABLE_LINKS"] = sharable_links_gof
    return task_dict


def CCBP_DRAFTS_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL1_ATTEMPTED"

    if not task_dict.get("CCBP_SHAREABLE_LINKS", {}).get("CCBP_INVITE_CODE"):
        import uuid
        invite_code = str(uuid.uuid4())[:8]

        sharable_links_gof = task_dict.get("CCBP_SHAREABLE_LINKS", {})

        sharable_links_gof["CCBP_INVITE_CODE"] = invite_code

        sharable_links_gof[
            "CCBP_OTG_WEBSITE"] = "https://www.onthegomodel.com/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_FREE_ACCESS_PORTAL"] = "https://webinar.ibhubs.co/xpm-ccbp-limited-access-portal/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_CCBP_WEBSITE"] = "https://www.onthegomodel.com/ccbp/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_MORE_DETAILS_ABOUT_PROGRAM"] = "https://www.onthegomodel.com/ccbp/program-videos/?prospect={}".format(
            invite_code)

        task_dict["CCBP_SHAREABLE_LINKS"] = sharable_links_gof
    return task_dict


def CCBP_LEADS_Make_Call_1(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL1_ATTEMPTED"
    task_dict['CCBP_LEAD_DETAILS']['CCBP_CLOSENESS'] = "Moderate"
    return task_dict


def CCBP_LEADS_Discard(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_DISCARDED"
    return task_dict


def CCBP_CALL1_ATTEMPTED_UnReachable(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL1_REATTEMPT"
    return task_dict


def CCBP_CALL1_ATTEMPTED_Not_interested(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_CALL1_ATTEMPTED_Sent_Video(task_dict, global_constants,
                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_MAKE_CALL2"
    task_dict['CCBP_CALL1_DETAILS']['CCBP_CALL1_REMARKS'] = "Updated Remarks"
    return task_dict


def CCBP_CALL1_REATTEMPT_UnReachable(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL1_REATTEMPT"
    return task_dict


def CCBP_CALL1_REATTEMPT_Not_interested(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_CALL1_REATTEMPT_Sent_Video(task_dict, global_constants,
                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_MAKE_CALL2"
    return task_dict


def CCBP_MAKE_CALL2_Make_Call_2(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL2_ATTEMPTED"
    task_dict['CCBP_CALL1_DETAILS'] = {
        "CCBP_CALL1_STATUS": "No",
        "CCBP_CALL1_REMARKS": "Some Thing Some Thing"
    }
    return task_dict


def CCBP_CALL2_ATTEMPTED_UnReachable(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL2_REATTEMPT"
    return task_dict


def CCBP_CALL2_ATTEMPTED_Not_interested(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_CALL2_ATTEMPTED_Want_to_explore_more(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_EXPLORING_FREE_ACCESS"
    return task_dict


def CCBP_CALL2_ATTEMPTED_Decision_Pending(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_FOLLOWUP_CALL"
    return task_dict


def CCBP_CALL2_ATTEMPTED_Interested_in_course(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_REGISTRATION_PENDING"
    task_dict['CCBP_RESISTANCES'] = [
        {
            "CCBP_RESISTANCES": "Time",
            "CCBP_RESISTANCES_REMARKS": "He is feeling tensed with time"
        }
    ]
    return task_dict


def CCBP_CALL2_REATTEMPT_UnReachable(task_dict, global_constants,
                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL2_REATTEMPT"
    return task_dict


def CCBP_CALL2_REATTEMPT_Not_interested(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_CALL2_REATTEMPT_Want_to_explore_more(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_EXPLORING_FREE_ACCESS"
    return task_dict


def CCBP_CALL2_REATTEMPT_Decision_Pending(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_FOLLOWUP_CALL"
    return task_dict


def CCBP_CALL2_REATTEMPT_Interested_in_course(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_REGISTRATION_PENDING"
    return task_dict


def CCBP_REGISTRATION_PENDING_Registration_complete(task_dict,
                                                    global_constants,
                                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_SUCCESSFUL_LEAD"
    return task_dict


def CCBP_REGISTRATION_PENDING_Not_interested(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_EXPLORING_FREE_ACCESS_Decision_Pending(task_dict, global_constants,
                                                stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_FOLLOWUP_CALL"
    return task_dict


def CCBP_EXPLORING_FREE_ACCESS_Interested_in_course(task_dict,
                                                    global_constants,
                                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_REGISTRATION_PENDING"
    return task_dict


def CCBP_EXPLORING_FREE_ACCESS_Not_interested(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_EXPLORING_FREE_ACCESS_Registration_complete(task_dict,
                                                     global_constants,
                                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_SUCCESSFUL_LEAD"
    return task_dict


def CCBP_FOLLOWUP_CALL_Interested_in_course(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_REGISTRATION_PENDING"
    return task_dict


def CCBP_FOLLOWUP_CALL_Not_interested(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEAD_LOST"
    return task_dict


def CCBP_FOLLOWUP_CALL_Registration_complete(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_SUCCESSFUL_LEAD"
    return task_dict


def CCBP_LEAD_LOST_Interested_in_course(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_REGISTRATION_PENDING"
    return task_dict


def CCBP_LEAD_LOST_Want_to_explore_more(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_EXPLORING_FREE_ACCESS"
    return task_dict


def CCBP_CREATE_LEAD_Save_as_Draft(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_DRAFTS"
    return task_dict


def CCBP_CREATE_LEAD_Make_Call_1(task_dict, global_constants,
                                 stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_CALL1_ATTEMPTED"

    if not task_dict.get("CCBP_SHAREABLE_LINKS", {}).get("CCBP_INVITE_CODE"):
        import uuid
        invite_code = str(uuid.uuid4())[:8]

        sharable_links_gof = task_dict.get("CCBP_SHAREABLE_LINKS", {})

        sharable_links_gof["CCBP_INVITE_CODE"] = invite_code

        sharable_links_gof[
            "CCBP_OTG_WEBSITE"] = "https://www.onthegomodel.com/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_FREE_ACCESS_PORTAL"] = "https://webinar.ibhubs.co/xpm-ccbp-limited-access-portal/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_CCBP_WEBSITE"] = "https://www.onthegomodel.com/ccbp/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_MORE_DETAILS_ABOUT_PROGRAM"] = "https://www.onthegomodel.com/ccbp/program-videos/?prospect={}".format(
            invite_code)

        task_dict["CCBP_SHAREABLE_LINKS"] = sharable_links_gof
    return task_dict


def CCBP_CREATE_LEAD_Create_Beneficiary(task_dict, global_constants,
                                        stage_value_dict):
    task_dict["status_variables"]["Status1"] = "CCBP_LEADS"

    if not task_dict.get("CCBP_SHAREABLE_LINKS", {}).get("CCBP_INVITE_CODE"):
        import uuid
        invite_code = str(uuid.uuid4())[:8]

        sharable_links_gof = task_dict.get("CCBP_SHAREABLE_LINKS", {})

        sharable_links_gof["CCBP_INVITE_CODE"] = invite_code

        sharable_links_gof[
            "CCBP_OTG_WEBSITE"] = "https://www.onthegomodel.com/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_FREE_ACCESS_PORTAL"] = "https://webinar.ibhubs.co/xpm-ccbp-limited-access-portal/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_CCBP_WEBSITE"] = "https://www.onthegomodel.com/ccbp/?prospect={}".format(
            invite_code)
        sharable_links_gof[
            "CCBP_MORE_DETAILS_ABOUT_PROGRAM"] = "https://www.onthegomodel.com/ccbp/program-videos/?prospect={}".format(
            invite_code)

        task_dict["CCBP_SHAREABLE_LINKS"] = sharable_links_gof
    return task_dict