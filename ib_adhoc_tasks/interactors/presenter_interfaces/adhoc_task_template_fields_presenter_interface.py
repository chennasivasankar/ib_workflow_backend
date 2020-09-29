import abc
from typing import List

from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO


class GetAdhocTaskTemplateFieldsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_adhoc_task_template_fields(
            self, field_dtos: List[FieldIdAndNameDTO]
    ):
        pass
