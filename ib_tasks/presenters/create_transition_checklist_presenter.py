from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId, \
    TransitionTemplateIsNotRelatedToGivenStageAction
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskTemplateIds, \
    InvalidTransitionChecklistTemplateId
from ib_tasks.interactors.presenter_interfaces \
    .create_transition_checklist_presenter_interface import \
    CreateOrUpdateTransitionChecklistTemplatePresenterInterface
from ib_tasks.presenters.mixins.gofs_fields_validation_presenter_mixin import \
    GoFsFieldsValidationPresenterMixin


class CreateOrUpdateTransitionChecklistTemplatePresenterImplementation(
    CreateOrUpdateTransitionChecklistTemplatePresenterInterface,
    HTTPResponseMixin, GoFsFieldsValidationPresenterMixin
):
    def raise_invalid_gof_ids(self, err):
        return self.raise_invalid_gof_ids_exception(err)

    def raise_invalid_field_ids(self, err):
        return self.raise_invalid_field_ids_exception(err)

    def raise_invalid_gofs_given_to_a_task_template(self, err):
        return self.raise_invalid_gofs_given_to_a_task_template_exception(err)

    def raise_duplicate_field_ids_to_a_gof(self, err):
        return self.raise_duplicate_field_ids_to_a_gof_exception(err)

    def raise_invalid_fields_given_to_a_gof(self, err):
        return self.raise_invalid_fields_given_to_a_gof_exception(err)

    def raise_user_needs_gof_writable_permission(self, err):
        return self.raise_user_needs_gof_writable_permission_exception(err)

    def raise_user_needs_field_writable_permission(self, err):
        return self.raise_user_needs_field_writable_permission_exception(err)

    def raise_empty_value_in_required_field(self, err):
        return self.raise_empty_value_in_required_field_exception(err)

    def raise_invalid_phone_number_value(self, err):
        return self.raise_invalid_phone_number_value_exception(err)

    def raise_invalid_email_address(self, err):
        return self.raise_invalid_email_address_exception(err)

    def raise_invalid_url_address(self, err):
        return self.raise_invalid_url_address_exception(err)

    def raise_weak_password(self, err):
        return self.raise_weak_password_exception(err)

    def raise_invalid_number_value(self, err):
        return self.raise_invalid_number_value_exception(err)

    def raise_invalid_float_value(self, err):
        return self.raise_invalid_float_value_exception(err)

    def raise_invalid_dropdown_value(self, err):
        return self.raise_invalid_dropdown_value_exception(err)

    def raise_invalid_name_in_gof_selector_field_value(self, err):
        return \
            self.raise_invalid_name_in_gof_selector_field_value_exception(err)

    def raise_invalid_choice_in_radio_group_field(self, err):
        return self.raise_invalid_choice_in_radio_group_field_exception(err)

    def raise_invalid_checkbox_group_options_selected(self, err):
        return self.raise_invalid_checkbox_group_options_selected_exception(
            err)

    def raise_invalid_multi_select_options_selected(self, err):
        return self.raise_invalid_multi_select_options_selected_exception(err)

    def raise_invalid_multi_select_labels_selected(self, err):
        return self.raise_invalid_multi_select_labels_selected_exception(err)

    def raise_invalid_time_format(self, err):
        return self.raise_invalid_time_format_exception(err)

    def raise_invalid_image_url(self, err):
        return self.raise_invalid_image_url_exception(err)

    def raise_not_acceptable_image_format(self, err):
        return self.raise_not_acceptable_image_format_exception(err)

    def raise_invalid_file_url(self, err):
        return self.raise_invalid_file_url_exception(err)

    def raise_not_acceptable_file_format(self, err):
        return self.raise_not_acceptable_file_format_exception(err)

    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        from ib_tasks.constants.exception_messages import \
            USER_DID_NOT_FILL_REQUIRED_FIELDS
        field_display_names = [
            dto.field_display_name for dto in err.unfilled_field_dtos]
        message = USER_DID_NOT_FILL_REQUIRED_FIELDS[0].format(
            field_display_names)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": USER_DID_NOT_FILL_REQUIRED_FIELDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_did_not_fill_required_gofs(
            self, err: UserDidNotFillRequiredGoFs):
        from ib_tasks.constants.exception_messages import \
            USER_DID_NOT_FILL_REQUIRED_GOFS
        message = USER_DID_NOT_FILL_REQUIRED_GOFS[0].format(
            err.gof_display_names)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": USER_DID_NOT_FILL_REQUIRED_GOFS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_display_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_DISPLAY_ID
        message = INVALID_TASK_DISPLAY_ID[0].format(err.task_display_id)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_DISPLAY_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_transition_checklist_template_id(
            self, err: InvalidTransitionChecklistTemplateId
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID
        response_message = INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID[0].format(
            err.transition_checklist_template_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_action(self, err: InvalidActionException):
        from ib_tasks.constants.exception_messages import \
            INVALID_ACTION_ID
        response_message = INVALID_ACTION_ID[0].format(err.action_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_ACTION_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_id(self, err: InvalidStageId):
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_ID
        response_message = INVALID_STAGE_ID[0].format(err.stage_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_STAGE_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_same_gof_order_for_a_gof(self,
                                       err: DuplicateSameGoFOrderForAGoF):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF
        response_message = DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF[0].format(
            err.gof_id, str(err.same_gof_orders))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_transition_template_is_not_related_to_given_stage_action(
            self, err: TransitionTemplateIsNotRelatedToGivenStageAction
    ):
        from ib_tasks.constants.exception_messages import \
            TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION
        response_message = \
            TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION[0].format(
                err.transition_checklist_template_id, err.stage_id,
                err.action_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status":
                TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def get_create_transition_checklist_response(self):
        data = {
            "message": "transition checklist created successfully"
        }
        return self.prepare_201_created_response(data)

    def raise_invalid_task_id(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_ID
        response_message = INVALID_TASK_ID[0].format(err.task_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_task_template_ids(self, err: InvalidTaskTemplateIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS
        response_message = INVALID_TASK_TEMPLATE_IDS[0].format(
            err.invalid_task_template_ids
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_TEMPLATE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)
