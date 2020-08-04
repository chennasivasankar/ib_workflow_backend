from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.presenter_interfaces.create_task_presenter import \
    CreateTaskPresenterInterface
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class CreateTaskPresenterImplementation(
    CreateTaskPresenterInterface, HTTPResponseMixin
):

    def get_create_task_response(self):
        data = {
            "message": "task created successfully"
        }
        return self.prepare_201_created_response(response_dict=data)

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

    def raise_invalid_action_id(self, err: InvalidActionException):
        from ib_tasks.constants.exception_messages import INVALID_ACTION_ID
        response_message = INVALID_ACTION_ID[0].format(err.action_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_ACTION_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gof_ids(self, err: InvalidGoFIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOF_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_field_ids(self, err: InvalidFieldIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELD_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gofs_given_to_a_task_template(
            self, err: InvalidGoFsOfTaskTemplate
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOFS_OF_TASK_TEMPLATE
        response_message = INVALID_GOFS_OF_TASK_TEMPLATE[0].format(
            str(err.gof_ids), err.task_template_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOFS_OF_TASK_TEMPLATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_field_ids_to_a_gof(self, err: DuplicateFieldIdsToGoF):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_GOF_IDS_GIVEN_TO_A_GOF
        response_message = DUPLICATE_GOF_IDS_GIVEN_TO_A_GOF[0].format(
            err.gof_id, str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_GOF_IDS_GIVEN_TO_A_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_fields_given_to_a_gof(self, err: InvalidFieldsOfGoF):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELDS_OF_TASK_TEMPLATE
        response_message = INVALID_FIELDS_OF_TASK_TEMPLATE[0].format(
            str(err.field_ids), err.gof_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELDS_OF_TASK_TEMPLATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_gof_writable_permission(
            self, err: UserNeedsGoFWritablePermission):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_GOF_WRITABLE_PERMISSION
        response_message = USER_NEEDS_GOF_WRITABLE_PERMISSION[0].format(
            err.user_id, err.gof_id, str(err.missed_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_GOF_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_field_writable_permission(
            self, err: UserNeedsFieldWritablePermission
    ):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_FILED_WRITABLE_PERMISSION
        response_message = USER_NEEDS_FILED_WRITABLE_PERMISSION[0].format(
            err.user_id, err.field_id, str(err.missed_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_FILED_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)
