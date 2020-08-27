def EMP_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_DRAFTS"
    return task_dict


def EMP_DRAFTS_Submit_for_Enrolling(task_dict, global_constants,
                                    stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_SELECTION_PROCESS"
    return task_dict


def EMP_PENDING_BACKGROUND_CHECK_Cleared(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PENDING_EMPLOYEE_ALIGNMENT_VALIDATION"
    return task_dict


def EMP_PENDING_BACKGROUND_CHECK_Not_Cleared(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_REJECTED"
    return task_dict


def EMP_PENDING_FINAL_SELECTION_Reject(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_REJECTED"
    return task_dict


def EMP_PENDING_FINAL_SELECTION_Selected(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "EMP_PENDING_ONBOARDING_SIGNING_AGREEMENTS"
    return task_dict


def EMP_PENDING_MENTOR_DISCUSSION_Interested(task_dict, global_constants,
                                             stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "EMP_PENDING_PAYMENT_INFORMATION"
    return task_dict


def EMP_PENDING_MENTOR_DISCUSSION_Not_Interested(task_dict, global_constants,
                                                 stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_REJECTED"
    return task_dict


def EMP_PENDING_ONBOARDING_SIGNING_AGREEMENTS_Submit(task_dict,
                                                     global_constants,
                                                     stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_BACKGROUND_CHECK"
    return task_dict


def EMP_PENDING_PAYMENT_INFORMATION_Submit(task_dict, global_constants,
                                           stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_TRAINING"
    return task_dict


def EMP_PENDING_SELECTION_PROCESS_Reject(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_REJECTED"
    return task_dict


def EMP_PENDING_SELECTION_PROCESS_Selected(task_dict, global_constants,
                                           stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_MENTOR_DISCUSSION"
    return task_dict


def EMP_PENDING_TRAINING_Submit(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_FINAL_SELECTION"
    return task_dict


def PENDING_EMPLOYEE_ALIGNMENT_VALIDATION_Aligned(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PENDING_EMPLOYEE_ASSIGNMENT_COMPLETION"
    return task_dict


def PENDING_EMPLOYEE_ASSIGNMENT_COMPLETION_Submit(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PENDING_SALARY_DEPOSIT"
    return task_dict


def PENDING_EXTRA_ASSIGNMENT_COMPLETION_Submit(task_dict, global_constants,
                                               stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PENDING_LEARNINGS_FOR_WEEK"
    return task_dict


def PENDING_LEARNINGS_FOR_WEEK_Submit(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PENDING_EMPLOYEE_ALIGNMENT_VALIDATION"
    return task_dict


def PENDING_SALARY_DEPOSIT_Submit(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PENDING_WEEKLY_TARGET_COMPLETION"
    return task_dict


def PENDING_WEEKLY_TARGET_COMPLETION_Submit(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PENDING_EXTRA_ASSIGNMENT_COMPLETION"
    return task_dict


def PR_CREATE_EMPLOYEE_FORM_Save_as_Draft(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_DRAFTS"
    return task_dict


def PR_CREATE_EMPLOYEE_FORM_Submit_for_Enrolling(task_dict, global_constants,
                                                 stage_value_dict):
    task_dict["status_variables"]["Status1"] = "EMP_PENDING_SELECTION_PROCESS"
    return task_dict


def PR_CREATE_PAYMENT_REQUEST_Save_as_Draft(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
    return task_dict


def PR_CREATE_PAYMENT_REQUEST_Submit_for_Approval(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


def PR_CREATE_VENDOR_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
    return task_dict


def PR_CREATE_VENDOR_Submit(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
    return task_dict


def PR_NEED_CLARIFICATION_Discard(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
    return task_dict


def PR_NEED_CLARIFICATION_Submit_for_Approval(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Discard(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
    return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Save_Draft(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
    return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Submit_for_Approval(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION"
    task_dict["status_variables"][
        "Status9"] = PR_ACCOUNTS_LEVEL1_VERIFICATION_DONE
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PR_PENDING_ACCOUNTS_LEVEL3_VERIFICATION"
    task_dict["status_variables"][
        "Status5"] = "PR_PENDING_ACCOUNTS_LEVEL4_VERIFICATION"
    task_dict["status_variables"][
        "Status10"] = PR_ACCOUNTS_LEVEL2_VERIFICATION_DONE
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL3_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PR_ACCOUNTS_LEVEL3_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status5"] == "PR_ACCOUNTS_LEVEL4_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status6"] = "PR_ACCOUNTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL4_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status5"] = "PR_ACCOUNTS_LEVEL4_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status1"] == "PR_ACCOUNTS_LEVEL3_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status6"] = "PR_ACCOUNTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_COMPLIANCE_APPROVAL_Verify(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"][
        "Status4"] = "PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION"

    return task_dict


def PR_PENDING_OVERALL_FINANCE_RP_APPROVAL_Approve(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"]["Status8"] = "PR_PENDING_PAYMENTS_PROCESSING"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL1_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status2"] = "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE" and (
                task_dict["status_variables"]["Status4"]
                == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE"
                or task_dict["status_variables"]["Status4"]
                == "PR_PAYMENTS_LEVEL5_APPROVAL_DONE"):
        task_dict["status_variables"][
            "Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL2_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status3"] = "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and (
                task_dict["status_variables"]["Status4"]
                == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE"
                or task_dict["status_variables"]["Status4"]
                == "PR_PAYMENTS_LEVEL5_APPROVAL_DONE"):
        task_dict["status_variables"][
            "Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Agreement_Mismatch(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status4"] = "PR_PENDING_COMPLIANCE_APPROVAL"

    return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Approve(task_dict,
                                                    global_constants,
                                                    stage_value_dict):
    if task_dict["FIN_VENDOR_PAYMENT_DETAILS"][
            "FIN_REQUESTED_AMOUNT"] < global_constants[
                "PAYABLE_AMOUNT_WITHOUT_APPROVAL"]:
        task_dict["status_variables"][
            "Status4"] = "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE"
    else:
        task_dict["status_variables"][
            "Status4"] = "PR_PENDING_PAYMENTS_LEVEL5_APPROVAL"

    if task_dict["status_variables"][
            "Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and task_dict[
                "status_variables"][
                    "Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE" and task_dict[
                        "status_variables"][
                            "Status4"] == "PR_PAYMENTS_LEVEL3_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Reject(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status4"] = "PR_PENDING_PAYMENTS_LEVEL5_APPROVAL"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL5_APPROVAL_Approve(task_dict, global_constants,
                                                stage_value_dict):
    task_dict["status_variables"][
        "Status4"] = "PR_PAYMENTS_LEVEL5_APPROVAL_DONE"

    if task_dict["status_variables"][
            "Status2"] == "PR_PAYMENTS_LEVEL1_VERIFICATION_DONE" and task_dict[
                "status_variables"][
                    "Status3"] == "PR_PAYMENTS_LEVEL2_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status7"] = "PR_PAYMENTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status7"] == "PR_PAYMENTS_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status6"] == "PR_ACCOUNTS_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status7"] = "PR_PENDING_OVERALL_FINANCE_RP_APPROVAL"
    return task_dict


def PR_PENDING_PAYMENTS_LEVEL5_APPROVAL_Reject(task_dict, global_constants,
                                               stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_REJECTION_LIST"
    task_dict["status_variables"]["Status2"] = "PR_REJECTION_LIST"
    task_dict["status_variables"]["Status3"] = "PR_REJECTION_LIST"
    task_dict["status_variables"]["Status4"] = "PR_REJECTION_LIST"
    task_dict["status_variables"]["Status5"] = "PR_REJECTION_LIST"
    task_dict["status_variables"]["Status6"] = "PR_REJECTION_LIST"
    return task_dict


def PR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"][
        "Status2"] = "PR_PENDING_PAYMENTS_LEVEL1_VERIFICATION"
    task_dict["status_variables"][
        "Status3"] = "PR_PENDING_PAYMENTS_LEVEL2_VERIFICATION"
    task_dict["status_variables"][
        "Status4"] = "PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION"
    task_dict["status_variables"][
        "Status1"] = "PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION"
    return task_dict


def PR_PENDING_RP_APPROVAL_Need_Clarification(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_NEED_CLARIFICATION"
    return task_dict


def PR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_REJECTION_LIST"
    return task_dict


def VENDOR_DRAFTS_Discard(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DISCARDED"
    return task_dict


def VENDOR_DRAFTS_Save_Draft(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
    return task_dict


def VENDOR_DRAFTS_Submit_(task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
    return task_dict


def VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION_Verify(task_dict,
                                                       global_constants,
                                                       stage_value_dict):
    task_dict["status_variables"][
        "Status3"] = "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"
    return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION_Verify(task_dict,
                                                       global_constants,
                                                       stage_value_dict):
    task_dict["status_variables"][
        "Status2"] = "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status1"] == "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"
    return task_dict


def VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION_Verify(task_dict,
                                                       global_constants,
                                                       stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "VENDOR_PAYMENTS_LEVEL5_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status2"] == "VENDOR_PAYMENTS_LEVEL4_VERIFICATION_COMPLETED" and task_dict[
                "status_variables"][
                    "Status3"] == "VENDOR_ACCOUNTS_LEVEL5_VERIFICATION_COMPLETED":
        task_dict["status_variables"][
            "Status4"] = "VENDOR_VERIFICATION_COMPLETED"

    return task_dict


def VENDOR_PENDING_RP_APPROVAL_Approve(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
    task_dict["status_variables"][
        "Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
    task_dict["status_variables"][
        "Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"

    return task_dict


def VENDOR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_REJECTED"
    return task_dict
