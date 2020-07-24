from typing import List

from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface


class GetFieldsDetails:

    def __init__(self, user_id: str, field_ids:List[str],
                 storage: StorageInterface):
        self.user_id = user_id
        self.field_ids = field_ids
        self.storage = storage

    def get_fields_details(self):
        pass
