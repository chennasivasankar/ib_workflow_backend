

def PR_PAYMENT_REQUEST_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
	return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Submit_for_Approval(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
	return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
	return task_dict


def PR_PENDING_RP_APPROVAL_Need_Clarification(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_NEED_CLARIFICATION"
	return task_dict


def PR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_REJECTION_LIST"
	return task_dict


def PR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "PR_PENDING_PAYMENTS_LEVEL1_VERIFICATION"
	task_dict["status_variables"]["Status3"] = "PR_PENDING_PAYMENTS_LEVEL2_VERIFICATION"
	task_dict["status_variables"]["Status4"] = "PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION"
	task_dict["status_variables"]["Status1"] = "PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION"
	return task_dict


def PR_NEED_CLARIFICATION_Submit_for_Approval(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
	return task_dict


def PR_NEED_CLARIFICATION_Discard(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
	return task_dict


def PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION"
	task_dict["status_variables"]["Status9"] =PR_ACCOUNTS_LEVEL1_VERIFICATION_DONE
	return task_dict


def PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PENDING_ACCOUNTS_LEVEL3_VERIFICATION"
	task_dict["status_variables"]["Status5"] = "PR_PENDING_ACCOUNTS_LEVEL4_VERIFICATION"
	task_dict["status_variables"]["Status10"] = PR_ACCOUNTS_LEVEL2_VERIFICATION_DONE
	return task_dict


def PR_PENDING_ACCOUNTS_LEVEL3_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_ACCOUNTS_LEVEL3_VERIFICATION_DONE"
	
	if task_dict["status_variables"]["Status5"] == "PR_ACCOUNTS_LEVEL4_VERIFICATION_DONE":
	    task_dict["status_variables"]["Status6"] = "PR_ACCOUNTS_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_ACCOUNTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status5"] = "PR_ACCOUNTS_LEVEL4_VERIFICATION_DONE"
	
	if task_dict["status_variables"]["Status1"] == "PR_ACCOUNTS_LEVEL3_VERIFICATION_DONE":
	    task_dict["status_variables"]["Status6"] = "PR_ACCOUNTS_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL1_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status2"] = "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE"
	
	if task_dict["status_variables"]["Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE" and (task_dict["status_variables"]["Status4"] == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE" or task_dict["status_variables"]["Status4"] == "PR_PAYMENTS_LEVEL5_APPROVAL_DONE") :
	    task_dict["status_variables"]["Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"
	
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL2_VERIFICATION_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status3"] = "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE"
	
	if task_dict["status_variables"]["Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and (task_dict["status_variables"]["Status4"] == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE" or task_dict["status_variables"]["Status4"] == "PR_PAYMENTS_LEVEL5_APPROVAL_DONE") :
	    task_dict["status_variables"]["Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"
	
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Approve(task_dict, global_constants, stage_value_dict):
	if task_dict["FIN_VENDOR_PAYMENT_DETAILS"]["FIN_REQUESTED_AMOUNT"]          < global_constants["PAYABLE_AMOUNT_WITHOUT_APPROVAL"]:
	    task_dict["status_variables"]["Status4"] = "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE"
	else:
	    task_dict["status_variables"]["Status4"] = "PR_PENDING_PAYMENTS_LEVEL5_APPROVAL"
	
	if task_dict["status_variables"]["Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and  task_dict["status_variables"]["Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE" and  task_dict["status_variables"]["Status4"] == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE": 
	    task_dict["status_variables"]["Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"
	
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status4"] = "PR_PENDING_PAYMENTS_LEVEL5_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Agreement_Mismatch(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status4"] = "PR_PENDING_COMPLIANCE_APPROVAL"
	
	return task_dict


def PR_PENDING_COMPLIANCE_APPROVAL_Verify(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status4"] = "PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION"
	
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL5_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status4"] = "PR_PAYMENTS_LEVEL5_APPROVAL_DONE"
	
	if task_dict["status_variables"]["Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and  task_dict["status_variables"]["Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE" : 
	    task_dict["status_variables"]["Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"
	
	if task_dict["status_variables"]["Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict["status_variables"]["Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED" :
	    task_dict["status_variables"]["Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
	return task_dict


def PR_PENDING_PAYMENTS_LEVEL5_APPROVAL_Reject(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_REJECTION_LIST"
	task_dict["status_variables"]["Status2"] = "PR_REJECTION_LIST"
	task_dict["status_variables"]["Status3"] = "PR_REJECTION_LIST"
	task_dict["status_variables"]["Status4"] = "PR_REJECTION_LIST"
	task_dict["status_variables"]["Status5"] = "PR_REJECTION_LIST"
	task_dict["status_variables"]["Status6"] = "PR_REJECTION_LIST"
	return task_dict


def PR_PENDING_OVERALL_FINANCE_RP_APPROVAL_Approve(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status8"] = "PR_PENDING_PAYMENTS_PROCESSING"
	return task_dict


def PR_CREATE_PAYMENT_REQUEST_Save_as_Draft(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
	return task_dict


def PR_CREATE_PAYMENT_REQUEST_Submit_for_Approval(task_dict, global_constants, stage_value_dict):
	task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
	return task_dict
