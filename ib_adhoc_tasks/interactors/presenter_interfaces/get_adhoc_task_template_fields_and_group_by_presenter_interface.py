import abc

from ib_adhoc_tasks.interactors.dtos.dtos import \
    TemplateFieldsAndGroupByFieldsDTO


class GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_template_and_group_by_fields(
            self,
            template_fields_and_group_by_fields_dto:
            TemplateFieldsAndGroupByFieldsDTO
    ):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_allowed_to_create_more_than_one_group_by_in_list_view(
            self
    ):
        pass

    @abc.abstractmethod
    def get_response_for_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view(
            self
    ):
        pass
