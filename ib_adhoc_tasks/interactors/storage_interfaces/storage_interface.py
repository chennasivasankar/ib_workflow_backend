import abc
from typing import List

from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByDetailsDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_group_by_details_dtos(
            self, user_id: str
    ) -> List[GroupByDetailsDTO]:
        pass
