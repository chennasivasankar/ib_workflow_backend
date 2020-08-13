def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
    return task_dict


def VENDOR_DRAFTS_Submit_for_Approval(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
    return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
    return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
    return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL_5_VERIFICATION"
    task_dict["status_variables"][
        "Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL_4_VERIFICATION"
    task_dict["status_variables"][
        "Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL_5_VERIFICATION"

    return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL_5_VERIFICATION_Verify(task_dict,
                                                        global_constants,
                                                        stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "VENDOR_PAYMENTS_LEVEL_5_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
        "Status2"] == "VENDOR_PAYMENTS_LEVEL_4_VERIFICATION_COMPLETED" and \
            task_dict["status_variables"][
                "Status3"] == "VENDOR_ACCOUNTS_LEVEL_5_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"

    return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL_4_VERIFICATION_Verify(task_dict,
                                                        global_constants,
                                                        stage_value_dict):
    task_dict["status_variables"][
        "Status2"] = "VENDOR_PAYMENTS_LEVEL_4_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
        "Status1"] == "VENDOR_PAYMENTS_LEVEL_5_VERIFICATION_COMPLETED" and \
            task_dict["status_variables"][
                "Status3"] == "VENDOR_ACCOUNTS_LEVEL_5_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"
    return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL_5_VERIFICATION_Verify(task_dict,
                                                        global_constants,
                                                        stage_value_dict):
    task_dict["status_variables"][
        "Status3"] = "VENDOR_ACCOUNTS_LEVEL_5_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
        "Status1"] == "VENDOR_PAYMENTS_LEVEL_5_VERIFICATION_COMPLETED" and \
            task_dict["status_variables"][
                "Status2"] == "VENDOR_PAYMENTS_LEVEL_4_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"
    return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
	return task_dict


def VENDOR_DRAFTS_Submit_for_Approval(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
	return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
	task_dict["status_variables"]["Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
	return task_dict


def VENDOR_DRAFTS_Submit_(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
	return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
	task_dict["status_variables"]["Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
	return task_dict


def VENDOR_DRAFTS_Submit_(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
	return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
	task_dict["status_variables"]["Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
	return task_dict


def VENDOR_DRAFTS_Submit_(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
	return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
	task_dict["status_variables"]["Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
	return task_dict


def VENDOR_DRAFTS_Submit_(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
	return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
	return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
	task_dict["status_variables"]["Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	
	return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
	    task_dict["status_variables"]["Status4"] = "VENDOR_VERIFICATION_COMPLETED"
	return task_dict
