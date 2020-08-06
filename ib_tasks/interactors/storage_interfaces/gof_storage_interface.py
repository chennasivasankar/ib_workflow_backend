import abc
from typing import List

from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRoleDTO, GoFToTaskTemplateDTO


class GoFStorageInterface(abc.ABC):
    @abc.abstractmethod
    def get_existing_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def create_gof_roles(self, gof_role_dtos: List[GoFRoleDTO]):
        pass

    @abc.abstractmethod
    def update_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def delete_gof_roles(self, gof_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_existing_gof_ids(self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_gofs_details_dtos_for_given_gof_ids(
            self, gof_ids: List[str]) -> List[GoFDTO]:
        pass

    @abc.abstractmethod
    def get_gofs_to_task_templates_from_permitted_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gof_ids_with_read_permission_for_user(self, roles: List[str]) -> \
            List[str]:
        pass

    @abc.abstractmethod
    def get_valid_gof_ids_in_given_gof_ids(
            self, gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_gof_dtos_for_given_gof_ids(
            self, gof_ids: List[str]
    ) -> List[GoFDTO]:
        pass