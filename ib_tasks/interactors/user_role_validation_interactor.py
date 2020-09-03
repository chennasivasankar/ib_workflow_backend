from typing import List

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO, TaskProjectRolesDTO


class UserRoleValidationInteractor:
    def does_user_has_required_permission(self, user_id: str,
                                          role_ids: List[str]) -> bool:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        if ALL_ROLES_ID in role_ids:
            return True

        user_role_ids = self._get_user_role_ids(user_id)
        if set(user_role_ids).intersection(set(role_ids)):
            return True
        return False

    def get_gof_ids_having_read_permission_for_user(
            self, user_id: str, gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        gof_ids_of_user_with_read_permission = \
            gof_storage.get_gof_ids_having_read_permission_for_user(
                user_roles=user_role_ids, gof_ids=gof_ids)

        return gof_ids_of_user_with_read_permission

    def get_gof_ids_having_write_permission_for_user(
            self, user_id: str, gof_ids: List[str],
            gof_storage: GoFStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        gof_ids_of_user_with_write_permission = \
            gof_storage.get_gof_ids_having_write_permission_for_user(
                user_roles=user_role_ids, gof_ids=gof_ids)

        return gof_ids_of_user_with_write_permission

    def get_field_ids_having_read_permission_for_user(
            self, user_id: str, field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        field_ids_having_read_permission_for_user = \
            field_storage.get_field_ids_having_read_permission_for_user(
                user_roles=user_role_ids, field_ids=field_ids)

        return field_ids_having_read_permission_for_user

    def get_field_ids_having_write_permission_for_user(
            self, user_id: str, field_ids: List[str],
            field_storage: FieldsStorageInterface) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id)
        field_ids_having_write_permission_for_user = \
            field_storage.get_field_ids_having_write_permission_for_user(
                user_roles=user_role_ids, field_ids=field_ids)

        return field_ids_having_write_permission_for_user

    def get_field_ids_having_permission_for_user(
            self, user_id: str, field_ids: List[str],
            task_project_dtos: List[TaskProjectDTO],
            field_storage: FieldsStorageInterface) -> List[str]:

        project_ids = [task.project_id for task in task_project_dtos]
        user_role_ids = self._get_user_role_ids_for_project_ids(
            user_id, project_ids)
        task_project_roles = self._get_task_project_roles_dtos(user_role_ids,
                                                               task_project_dtos)
        field_ids_having_permission_for_user = \
            field_storage.get_field_ids_permissions_for_user_in_projects(
                task_project_roles=task_project_roles, field_ids=field_ids)

        return field_ids_having_permission_for_user

    def check_is_user_has_read_permission_for_field(
            self, user_id: str, field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        user_role_ids = self._get_user_role_ids(user_id)
        is_user_has_read_permission = \
            field_storage.check_is_user_has_read_permission_for_field(
                field_id=field_id, user_roles=user_role_ids)
        return is_user_has_read_permission

    def check_is_user_has_write_permission_for_field(
            self, user_id: str, field_id: str,
            field_storage: FieldsStorageInterface) -> bool:

        user_role_ids = self._get_user_role_ids(user_id)
        is_user_has_write_permission = \
            field_storage.check_is_user_has_write_permission_for_field(
                field_id=field_id, user_roles=user_role_ids)
        return is_user_has_write_permission

    def get_permitted_stage_ids_given_user_id(self, user_id: str,
                                              project_id: str,
                                              stage_storage: StageStorageInterface) -> List[str]:
        user_role_ids = self._get_user_role_ids_for_project(user_id,
                                                            project_id)
        permitted_stage_ids = stage_storage.get_permitted_stage_ids(
            user_role_ids, project_id
        )
        return permitted_stage_ids

    def get_permitted_action_ids_for_given_user_id(
            self, stage_ids: List[str],
            user_id: str, project_id: str,
            action_storage: ActionStorageInterface) -> List[int]:
        user_role_ids = self._get_user_role_ids_for_project(
            user_id, project_id)
        permitted_action_ids = action_storage.\
            get_permitted_action_ids_given_stage_ids(
            user_role_ids, stage_ids)
        return permitted_action_ids

    def get_permitted_action_ids_for_given_user_in_projects(
            self, stage_ids: List[str],
            user_id: str, task_project_dtos: List[TaskProjectDTO],
            action_storage: ActionStorageInterface) -> List[int]:
        project_ids = [task.project_id for task in task_project_dtos]
        user_project_roles = self._get_user_role_ids_for_project_ids(
            user_id, project_ids)
        task_project_roles = self._get_task_project_roles_dtos(user_project_roles,
                                                               task_project_dtos)
        permitted_action_ids = action_storage. \
            get_permitted_action_ids_for_given_task_stages(
            task_project_roles, stage_ids)
        return permitted_action_ids

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids

    @staticmethod
    def _get_user_role_ids_for_project(user_id: str, project_id: str) -> \
            List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids_based_on_project(
                user_id=user_id,
                project_id=project_id)
        return user_role_ids

    @staticmethod
    def _get_user_role_ids_for_project_ids(user_id: str, project_ids: List[str]) -> \
            List[ProjectRolesDTO]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        project_roles_dtos = \
            roles_service.get_user_role_ids_based_on_given_project_ids(
                user_id=user_id,
                project_ids=project_ids)
        return project_roles_dtos

    @staticmethod
    def _get_task_project_roles_dtos(user_project_roles: List[ProjectRolesDTO],
                                     task_project_dtos: List[TaskProjectDTO]) -> \
            List[TaskProjectRolesDTO]:
        task_project_roles_dtos = []
        for user_project, task_project in zip(user_project_roles, task_project_dtos):
            if user_project.project_id == task_project.project_id:
                task_project_roles_dtos.append(
                    TaskProjectRolesDTO(
                        task_id=task_project.task_id,
                        project_id=user_project.project_id,
                        roles=user_project.roles
                    )
                )
        return task_project_roles_dtos
