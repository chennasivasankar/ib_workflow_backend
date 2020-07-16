from typing import List

import json

from ib_tasks.interactors.dtos.dtos import FieldDTO

from ib_tasks.interactors.storage_interfaces.create_fields_storage_interface \
    import CreateFieldsStorageInterface


class CreateFieldsStorageImplementation(CreateFieldsStorageInterface):

    def get_available_roles(self) -> List[str]:
        pass

    def create_fields(self, field_dtos: List[FieldDTO]):
        pass
