import abc
from typing import List

from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFRoleDTO, GoFToTaskTemplateDTO, GoFIdWithGoFDisplayNameDTO, \
    GoFIdWithTaskGoFIdDTO


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
    def get_gofs_to_templates_from_permitted_gofs(
            self, gof_ids: List[str]) -> List[GoFToTaskTemplateDTO]:
        pass

    @abc.abstractmethod
    def get_gof_ids_with_read_permission_for_user(
            self, user_roles: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_permitted_template_gof_dtos(
            self, user_roles: List[str], template_ids: List[str]
    ):
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

    @abc.abstractmethod
    def get_gof_ids_having_read_permission_for_user(
            self, user_roles: List[str], gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_gof_ids_having_write_permission_for_user(
            self, user_roles: List[str], gof_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_write_permitted_gof_ids_in_given_gof_ids(
            self, user_roles: List[str], template_gof_ids: List[str]
    ) -> List[GoFIdWithGoFDisplayNameDTO]:
        pass

    @abc.abstractmethod
    def get_filled_task_gofs_with_gof_id(
            self, task_id: int) -> List[GoFIdWithTaskGoFIdDTO]:
        pass

    @abc.abstractmethod
    def get_filled_field_ids_of_given_task_gof_ids(
            self, task_gof_ids: List[int]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_gof_ids_for_given_template(self, template_id: str) -> List[str]:
        pass
