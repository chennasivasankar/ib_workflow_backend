def PR_PAYMENT_REQUEST_DRAFTS_Save_Draft(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
    return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Submit_for_Approval(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


def PR_PAYMENT_REQUEST_DRAFTS_Discard(task_dict, global_constants,
                                      stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
    return task_dict


def PR_PENDING_RP_APPROVAL_Need_Clarification(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_NEED_CLARIFICATION"
    return task_dict


def PR_PENDING_RP_APPROVAL_Reject(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_REJECTION_LIST"
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


def PR_NEED_CLARIFICATION_Submit_for_Approval(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


def PR_NEED_CLARIFICATION_Discard(task_dict, global_constants,
                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_DISCARDED"
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL1_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION"
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL2_VERIFICATION_Verify(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status1"] = "PR_PENDING_ACCOUNTS_LEVEL3_VERIFICATION"
    task_dict["status_variables"][
        "Status5"] = "PR_PENDING_ACCOUNTS_LEVEL4_VERIFICATION"
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


def PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION_Agreement_Mismatch(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status4"] = "PR_PENDING_COMPLIANCE_APPROVAL"

    return task_dict


def PR_PENDING_COMPLIANCE_APPROVAL_Verify(task_dict, global_constants,
                                          stage_value_dict):
    task_dict["status_variables"][
        "Status4"] = "PR_PENDING_PAYMENTS_LEVEL3_VERIFICATION"

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


def PR_PENDING_OVERALL_FINANCE_RP_APPROVAL_Approve(task_dict, global_constants,
                                                   stage_value_dict):
    task_dict["status_variables"][
        "Status7"] = "PR_PAYMENTS_ACCOUNTS_VERIFICATION_COMPLETED"
    task_dict["status_variables"]["Status8"] = "PR_PENDING_PAYMENTS_PROCESSING"
    return task_dict


def PR_PENDING_PAYMENTS_PROCESSING_Initiate_Payment(task_dict,
                                                    global_constants,
                                                    stage_value_dict):
    if task_dict["FIN_PAYMENT_TYPE"][
            "FIN_TYPE_OF_PAYMENT_REQUEST"] == "Vendor Payment":
        task_dict["status_variables"][
            "Status8"] = "PR_UPDATE_INITIATION_STATUS"
    elif task_dict["FIN_PAYMENT_TYPE"][
            "FIN_TYPE_OF_PAYMENT_REQUEST"] == "Online Order":
        task_dict["status_variables"][
            "Status8"] = "PR_UPLOAD_INVOICES_AND_STATUS"
    return task_dict


def PR_UPDATE_INITIATION_STATUS_Update_Initiation_Status(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status8"] = "PR_UPDATE_AUTHORIZATION_STATUS"
    return task_dict


def PR_UPDATE_AUTHORIZATION_STATUS_Update_Authorization_Status(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_UPLOAD_BANK_AND_CMS_STATEMENT"
    return task_dict


def PR_UPLOAD_INVOICES_AND_STATUS_Upload_Invoices(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_UPLOAD_BANK_AND_CMS_STATEMENT"
    return task_dict


def PR_UPLOAD_BANK_AND_CMS_STATEMENT_Upload_Bank_Statement(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL1_VERIFICATION"
    task_dict["status_variables"][
        "Status9"] = "PR_PENDING_INVOICES_VERIFICATION"
    return task_dict


def PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL1_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL2_VERIFICATION"
    return task_dict


def PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL2_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL3_VERIFICATION"
    task_dict["status_variables"][
        "Status10"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL4_VERIFICATION"
    return task_dict


def PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL3_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status8"] = "PR_POST_PAYMENTS_ACCOUNTS_LEVEL3_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status10"] == "PR_POST_PAYMENTS_ACCOUNTS_LEVEL4_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status11"] = "PR_POST_PAYMENTS_ACCOUNTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status11"] == "PR_POST_PAYMENTS_ACCOUNTS_VERIFICATION_COMPLETED" and task_dict[
                "FIN_VENDOR_PAYMENT_DETAILS"][
                    "FIN_REQUESTED_AMOUNT"] < global_constants[
                        "PAYABLE_AMOUNT_WITHOUT_APPROVAL"]:
        task_dict["status_variables"][
            "Status11"] = "PR_PENDING_EXPORTING_FINAL_ACCOUNTS"
    else:
        task_dict["status_variables"][
            "Status11"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL5_VERIFICATION"
    return task_dict


def PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL4_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status10"] = "PR_POST_PAYMENTS_ACCOUNTS_LEVEL4_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status8"] == "PR_POST_PAYMENTS_ACCOUNTS_LEVEL3_VERIFICATION_DONE":
        task_dict["status_variables"][
            "Status11"] = "PR_POST_PAYMENTS_ACCOUNTS_VERIFICATION_COMPLETED"

    if task_dict["status_variables"][
            "Status11"] == "PR_POST_PAYMENTS_ACCOUNTS_VERIFICATION_COMPLETED" and task_dict[
                "FIN_VENDOR_PAYMENT_DETAILS"][
                    "FIN_REQUESTED_AMOUNT"] < global_constants[
                        "PAYABLE_AMOUNT_WITHOUT_APPROVAL"]:
        task_dict["status_variables"][
            "Status11"] = "PR_PENDING_EXPORTING_FINAL_ACCOUNTS"
    else:
        task_dict["status_variables"][
            "Status11"] = "PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL5_VERIFICATION"
    return task_dict


def PR_PENDING_POST_PAYMENTS_ACCOUNTS_LEVEL5_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"][
        "Status11"] = "PR_PENDING_EXPORTING_FINAL_ACCOUNTS"
    return task_dict


def PR_PENDING_EXPORTING_FINAL_ACCOUNTS_Export(task_dict, global_constants,
                                               stage_value_dict):
    task_dict["status_variables"]["Status11"] = "PR_UPDATE_ACCOUNTING_STATUS"
    return task_dict


def PR_UPDATE_ACCOUNTING_STATUS_Update(task_dict, global_constants,
                                       stage_value_dict):
    task_dict["status_variables"][
        "Status11"] = "PR_PENDING_FINAL_ACCOUNTS_VERIFICATION"
    return task_dict


def PR_PENDING_FINAL_ACCOUNTS_VERIFICATION_Verify(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"][
        "Status11"] = "PR_FINAL_ACCOUNTS_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status9"] == "PR_FINAL_FILING_VERIFICATION_DONE":
        task_dict["status_variables"]["Status11"] = "PR_COMPLETED"
    return task_dict


def PR_PENDING_INVOICES_VERIFICATION_Verify(task_dict, global_constants,
                                            stage_value_dict):
    if task_dict["FIN_VENDOR_PAYMENT_DETAILS"][
            "FIN_REQUESTED_AMOUNT"] < global_constants[
                "PAYABLE_AMOUNT_WITHOUT_APPROVAL"]:
        task_dict["status_variables"][
            "Status9"] = "PR_PENDING_FILING_OF_INVOICES"
    else:
        task_dict["status_variables"][
            "Status9"] = "PR_PENDING_ACCOUNTS_LEVEL2_INVOICES_VERIFICATION"
    return task_dict


def PR_PENDING_ACCOUNTS_LEVEL2_INVOICES_VERIFICATION_Verify(
        task_dict, global_constants, stage_value_dict):
    task_dict["status_variables"]["Status9"] = "PR_PENDING_FILING_OF_INVOICES"
    return task_dict


def PR_PENDING_FILING_OF_INVOICES_Verify(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"][
        "Status9"] = "PR_PENDING_FINAL_FILING_VERIFICATION"
    return task_dict


def PR_PENDING_FINAL_FILING_VERIFICATION_File(task_dict, global_constants,
                                              stage_value_dict):
    task_dict["status_variables"][
        "Status9"] = "PR_FINAL_FILING_VERIFICATION_DONE"

    if task_dict["status_variables"][
            "Status11"] == "PR_FINAL_ACCOUNTS_VERIFICATION_DONE":
        task_dict["status_variables"]["Status11"] = "PR_COMPLETED"
    return task_dict


def PR_CREATE_PAYMENT_REQUEST_Save_as_Draft(task_dict, global_constants,
                                            stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PAYMENT_REQUEST_DRAFTS"
    return task_dict


def PR_CREATE_PAYMENT_REQUEST_Submit_for_Approval(task_dict, global_constants,
                                                  stage_value_dict):
    task_dict["status_variables"]["Status1"] = "PR_PENDING_RP_APPROVAL"
    return task_dict


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
        "Status1"] = "VENDOR_PENDING_PAYMENTS_LEVEL5_VERIFICATION"
    task_dict["status_variables"][
        "Status2"] = "VENDOR_PENDING_PAYMENTS_LEVEL4_VERIFICATION"
    task_dict["status_variables"][
        "Status3"] = "VENDOR_PENDING_ACCOUNTS_LEVEL5_VERIFICATION"

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


def PR_CREATE_VENDOR_Save_as_Draft(task_dict, global_constants,
                                   stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_DRAFTS"
    return task_dict


def PR_CREATE_VENDOR_Submit_for_Approval(task_dict, global_constants,
                                         stage_value_dict):
    task_dict["status_variables"]["Status1"] = "VENDOR_PENDING_RP_APPROVAL"
    return task_dict
