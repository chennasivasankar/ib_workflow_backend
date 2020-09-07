def VENDOR_PENDING_RP_APPROVAL_Reject(
        task_dict, global_constants, stage_value_dict
):
	if task_dict["status_variables"]["Status1"]:
		task_dict["status_variables"]["Status1"] = "VENDOR"
	return task_dict
