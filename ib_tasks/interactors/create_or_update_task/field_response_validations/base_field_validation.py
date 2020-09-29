import abc
from typing import Optional, List

from ib_tasks.interactors.mixins.get_gofs_feilds_display_names_mixin import \
    GetGoFsFieldsDisplayNameMixin
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO


class BaseFieldValidation(abc.ABC, GetGoFsFieldsDisplayNameMixin):

    @abc.abstractmethod
    def validate_field_response(
            self,
            field_id_with_display_name_dtos: List[FieldWithGoFDisplayNameDTO]
    ) -> Optional[Exception]:
        pass
