import abc

from ib_tasks.exceptions.custom_exceptions import InvalidTaskTemplateIds, \
    InvalidFieldIds, InvalidGoFIds, EmptyValueForPlainTextField
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist


class CreateOrUpdateTaskPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_duplicate_field_ids(self, err: DuplicationOfFieldIdsExist):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_task_template_id(
            self, err: InvalidTaskTemplateIds
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_gof_ids(
        self, err: InvalidGoFIds
    ):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_field_ids(
            self, err: InvalidFieldIds
    ):
        pass

    @abc.abstractmethod
    def get_response_for_create_or_update_task(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_empty_value_in_plain_text_field(
            self, err: EmptyValueForPlainTextField
    ):
        pass
