from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import TeamDTO, RoleIdAndNameDTO, CompanyDTO


class GetUserOptionsStorageInterface(ABC):

    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_companies(self) -> List[CompanyDTO]:
        pass

    @abstractmethod
    def get_teams(self) -> List[TeamDTO]:
        pass

    @abstractmethod
    def get_roles(self) -> List[RoleIdAndNameDTO]:
        pass
