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
