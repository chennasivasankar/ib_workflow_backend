
from abc import ABC
from abc import abstractmethod
from typing import List


class StageStorageInterface(ABC):

    @abstractmethod
    def get_db_stage_ids(self, stage_ids: List[str]):
        pass