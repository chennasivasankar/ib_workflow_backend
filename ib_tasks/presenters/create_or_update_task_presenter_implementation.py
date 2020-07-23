
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds, \
    EmptyValueForPlainTextField
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds
from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
    import CreateOrUpdateTaskPresenterInterface
from django.http import response
import json


class CreateOrUpdateTaskPresenterImplementation(
    CreateOrUpdateTaskPresenterInterface
):
    def raise_exception_for_duplicate_field_ids(self, err: DuplicationOfFieldIdsExist):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_FIELD_IDS
        response_message = DUPLICATE_FIELD_IDS[0].format(
            str(err.field_ids)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": DUPLICATE_FIELD_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_task_template_id(
            self, err: InvalidTaskTemplateIds
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS
        response_message = INVALID_TASK_TEMPLATE_IDS[0].format(
            str(err.invalid_task_template_ids)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_TASK_TEMPLATE_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_gof_ids(self, err: InvalidGoFIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_GOF_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_field_ids(self, err: InvalidFieldIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_FIELD_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def get_response_for_create_or_update_task(self):
        pass

    def raise_exception_for_empty_value_in_plain_text_field(
            self, err: EmptyValueForPlainTextField
    ):
        from ib_tasks.constants.exception_messages import \
            EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD
        response_message = EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[0].format(
            str(err.field_id)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object
