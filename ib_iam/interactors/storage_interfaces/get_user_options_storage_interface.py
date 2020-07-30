from abc import ABC, abstractmethod
from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import RoleIdAndNameDTO, CompanyIdAndNameDTO, TeamIdAndNameDTO


class GetUserOptionsStorageInterface(ABC):

    @abstractmethod
    def check_is_admin_user(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_companies(self) -> List[CompanyIdAndNameDTO]:
        pass

    @abstractmethod
    def get_teams(self) -> List[TeamIdAndNameDTO]:
        pass

    @abstractmethod
    def get_roles(self) -> List[RoleIdAndNameDTO]:
        pass
