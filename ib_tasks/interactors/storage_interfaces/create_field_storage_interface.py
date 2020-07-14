import abc
from abc import ABC, abstractmethod

from typing import List


class CreateFieldStorageInterface(ABC):

    @abstractmethod
    def get_available_roles(self) -> List[str]:
        pass