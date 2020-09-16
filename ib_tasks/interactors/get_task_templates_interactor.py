from dataclasses import dataclass
from typing import List, Dict

from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    GetTaskTemplatesPresenterInterface, CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO, GoFDTO
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO, StageGoFWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


@dataclass
class GoFsDetailsWithFieldsDTO:
    gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO]
    gof_dtos: List[GoFDTO]
    field_with_is_field_writable_dtos: List[FieldPermissionDTO]


class GetTaskTemplatesInteractor:
    def __init__(
            self, task_storage: TaskStorageInterface,
            task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface,
            field_storage: FieldsStorageInterface,
            stage_storage: StageStorageInterface
    ):
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage
        self.stage_storage = stage_storage

    def get_task_templates_wrapper(
            self, user_id: str,
            presenter: GetTaskTemplatesPresenterInterface):

        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists
        try:
            complete_task_templates_dto = \
                self.get_task_templates(user_id=user_id)
        except TaskTemplatesDoesNotExists:
            return presenter.raise_task_templates_does_not_exists_exception()

        complete_task_templates_response_object = \
            presenter.get_task_templates_response(
                complete_task_templates_dto=complete_task_templates_dto
            )
        return complete_task_templates_response_object

    def get_task_templates(self, user_id: str):

        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        user_roles = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)

        complete_task_templates_dto = \
            self._get_complete_task_templates_dto(user_roles=user_roles)
        return complete_task_templates_dto

    def _get_complete_task_templates_dto(
            self, user_roles: List[str]) -> CompleteTaskTemplatesDTO:
        task_templates_dtos = \
            self.task_template_storage.get_task_templates_dtos()
        self._validate_task_templates_are_exists(
            task_templates_dtos=task_templates_dtos)

        project_id_with_task_template_id_dtos = \
            self.task_template_storage.\
            get_project_id_with_task_template_id_dtos()

        initial_stage_id_with_template_id_dtos = \
            self.task_storage.get_initial_stage_id_with_template_id_dtos()
        action_with_stage_id_dtos = self._get_action_with_stage_id_dtos(
            stage_id_with_template_id_dtos=
            initial_stage_id_with_template_id_dtos)

        task_template_ids = self._get_task_template_ids(
            task_templates_dtos=task_templates_dtos)
        gof_details_with_field_dto = \
            self._get_gof_details_with_field_dtos_of_task_templates(
                task_template_ids=task_template_ids, user_roles=user_roles)

        gofs_of_task_templates_dtos = \
            gof_details_with_field_dto.gofs_of_task_templates_dtos
        gof_ids = self._get_gof_ids_of_task_templates(
            gofs_of_task_templates_dtos=gofs_of_task_templates_dtos)
        stage_gof_with_template_id_dtos = \
            self._get_stage_gofs_for_each_task_template_dtos(
                task_template_ids=task_template_ids, gof_ids=gof_ids,
                user_roles=user_roles)

        return CompleteTaskTemplatesDTO(
            task_template_dtos=task_templates_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            initial_stage_id_with_template_id_dtos=
            initial_stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_details_with_field_dto.gof_dtos,
            gofs_of_task_templates_dtos=
            gof_details_with_field_dto.gofs_of_task_templates_dtos,
            field_with_permissions_dtos=
            gof_details_with_field_dto.field_with_is_field_writable_dtos,
            stage_gof_with_template_id_dtos=stage_gof_with_template_id_dtos)

    def _get_gof_details_with_field_dtos_of_task_templates(
            self, task_template_ids: List[str], user_roles: List[str]
    ) -> GoFsDetailsWithFieldsDTO:
        gof_ids_of_task_templates_having_user_permissions = \
            self._get_gof_ids_of_task_templates_having_user_permissions(
                task_template_ids=task_template_ids, user_roles=user_roles)
        field_with_permissions_dtos = \
            self._get_field_with_permissions_of_gofs_in_dtos(
                gof_ids=gof_ids_of_task_templates_having_user_permissions,
                user_roles=user_roles)

        gof_ids_with_at_least_one_field = \
            self._get_gof_ids_having_at_least_one_field(
                gof_ids=gof_ids_of_task_templates_having_user_permissions,
                field_with_permissions_dtos=field_with_permissions_dtos)
        gofs_of_task_templates_dtos = self.task_template_storage. \
            get_gofs_to_templates_from_permitted_gofs(
                gof_ids=gof_ids_with_at_least_one_field)
        gofs_details_dtos = \
            self.gof_storage.get_gofs_details_dtos_for_given_gof_ids(
                gof_ids=gof_ids_with_at_least_one_field)

        gofs_details_with_fields_dto = GoFsDetailsWithFieldsDTO(
            gof_dtos=gofs_details_dtos,
            gofs_of_task_templates_dtos=gofs_of_task_templates_dtos,
            field_with_is_field_writable_dtos=field_with_permissions_dtos
        )
        return gofs_details_with_fields_dto

    def _get_gof_ids_of_task_templates_having_user_permissions(
            self, task_template_ids: List[str],
            user_roles: List[str]) -> List[str]:
        user_role_validation_interactor = UserRoleValidationInteractor()

        gof_ids_of_task_templates = \
            self.task_template_storage.get_gof_ids_of_templates(
                template_ids=task_template_ids)
        gof_ids_having_read_permission_for_user = \
            user_role_validation_interactor. \
            get_gof_ids_having_read_permission_for_user(
                user_roles=user_roles, gof_ids=gof_ids_of_task_templates,
                gof_storage=self.gof_storage)

        return gof_ids_having_read_permission_for_user

    def _get_action_with_stage_id_dtos(
            self,
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> List[ActionWithStageIdDTO]:
        stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos)
        action_with_stage_id_dtos = \
            self.task_storage.get_actions_for_given_stage_ids_in_dtos(
                stage_ids=stage_ids)
        return action_with_stage_id_dtos

    def _get_field_with_permissions_of_gofs_in_dtos(
            self, gof_ids: List[str], user_roles: List[str]
    ) -> List[FieldPermissionDTO]:
        field_ids_of_gofs = \
            self.field_storage.get_field_ids_for_given_gofs(gof_ids=gof_ids)

        field_ids_having_read_permission_for_user, \
            field_ids_having_write_permission_for_user = \
            self._get_field_ids_having_read_or_write_permission_for_user(
                field_ids=field_ids_of_gofs, user_roles=user_roles)

        fields_of_gofs_having_user_permission = list(set(
            field_ids_having_write_permission_for_user +
            field_ids_having_read_permission_for_user))

        field_dtos = self.field_storage.get_field_dtos(
            field_ids=fields_of_gofs_having_user_permission)
        field_dtos = \
            self._remove_gof_ids_from_gof_selector_if_user_does_not_have_read_permission(
                field_dtos=field_dtos,
                gof_ids_having_user_read_permissions=gof_ids)

        field_with_is_field_writable_dtos = \
            self._get_field_with_is_field_writable_dtos(
                field_dtos=field_dtos,
                field_ids_having_write_permission_for_user=
                field_ids_having_write_permission_for_user
            )
        return field_with_is_field_writable_dtos

    def _get_field_ids_having_read_or_write_permission_for_user(
            self, field_ids: List[str], user_roles: List[str]):
        user_role_validation_interactor = UserRoleValidationInteractor()

        field_ids_having_write_permission_for_user = \
            user_role_validation_interactor. \
            get_field_ids_having_write_permission_for_user(
                user_roles=user_roles, field_ids=field_ids,
                field_storage=self.field_storage)
        field_ids_having_read_permission_for_user = \
            user_role_validation_interactor. \
            get_field_ids_having_read_permission_for_user(
                user_roles=user_roles, field_ids=field_ids,
                field_storage=self.field_storage)
        return field_ids_having_read_permission_for_user, \
            field_ids_having_write_permission_for_user

    def _remove_gof_ids_from_gof_selector_if_user_does_not_have_read_permission(
            self, field_dtos: List[FieldDTO],
            gof_ids_having_user_read_permissions: List[str]) -> List[FieldDTO]:
        import json
        from ib_tasks.constants.enum import FieldTypes
        for field_dto in field_dtos:
            is_field_is_gof_selector = \
                field_dto.field_type == FieldTypes.GOF_SELECTOR.value
            if is_field_is_gof_selector:
                field_values = json.loads(field_dto.field_values)
                gof_details = \
                    self._get_gof_details_with_user_permitted_gof_ids(
                        gof_details_dicts=field_values,
                        gof_ids_having_user_read_permissions=
                        gof_ids_having_user_read_permissions)
                field_dto.field_values = json.dumps(gof_details)
        return field_dtos

    def _get_stage_gofs_for_each_task_template_dtos(
            self, task_template_ids: List[str], gof_ids: List[str],
            user_roles: List[str]
    ) -> List[StageGoFWithTemplateIdDTO]:
        stage_id_with_template_id_dtos = \
            self.stage_storage.get_stage_id_with_template_id_dtos(
                task_template_ids=task_template_ids
            )

        user_permitted_stage_id_with_template_id_dtos = \
            self._get_user_permitted_stage_id_with_template_id_dtos(
                stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
                user_roles=user_roles)

        stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=
            user_permitted_stage_id_with_template_id_dtos)
        stage_gof_dtos = self.stage_storage.\
            get_stage_gof_dtos_for_given_stages_and_gofs(
                stage_ids=stage_ids, gof_ids=gof_ids)
        stage_id_with_template_id_dtos_dict = \
            self._make_stage_id_with_template_id_dtos_dict(
                stage_id_with_template_id_dtos=
                user_permitted_stage_id_with_template_id_dtos)
        stage_gof_with_template_id_dtos = [
            StageGoFWithTemplateIdDTO(
                stage_id=stage_gof_dto.stage_id,
                task_template_id=stage_id_with_template_id_dtos_dict[
                    stage_gof_dto.stage_id],
                gof_id=stage_gof_dto.gof_id
            )
            for stage_gof_dto in stage_gof_dtos
        ]
        return stage_gof_with_template_id_dtos

    def _get_user_permitted_stage_id_with_template_id_dtos(
            self, user_roles: List[str],
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> List[StageIdWithTemplateIdDTO]:
        stage_ids = self._get_stage_ids(
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos)

        user_role_validation_interactor = UserRoleValidationInteractor()
        user_permitted_stage_ids = user_role_validation_interactor.\
            get_user_permitted_stage_ids_in_given_stage_ids(
                user_roles=user_roles, stage_ids=stage_ids,
                stage_storage=self.stage_storage)

        user_permitted_stage_id_with_template_id_dtos = [
            stage_id_with_template_id_dto
            for stage_id_with_template_id_dto in stage_id_with_template_id_dtos
            if stage_id_with_template_id_dto.stage_id in
            user_permitted_stage_ids
        ]
        return user_permitted_stage_id_with_template_id_dtos

    @staticmethod
    def _make_stage_id_with_template_id_dtos_dict(
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> Dict:
        stage_id_with_template_id_dtos_dict = {
            stage_id_with_template_id_dto.stage_id:
                stage_id_with_template_id_dto.template_id
            for stage_id_with_template_id_dto in stage_id_with_template_id_dtos
        }
        return stage_id_with_template_id_dtos_dict

    @staticmethod
    def _validate_task_templates_are_exists(
            task_templates_dtos: List[TemplateDTO]):
        task_templates_are_empty = not task_templates_dtos
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists

        if task_templates_are_empty:
            raise TaskTemplatesDoesNotExists()

    @staticmethod
    def _get_gof_ids_of_task_templates(
            gofs_of_task_templates_dtos: List[GoFToTaskTemplateDTO]
    ) -> List[str]:
        gof_ids = [
            gofs_to_task_templates_dto.gof_id
            for gofs_to_task_templates_dto in gofs_of_task_templates_dtos
        ]
        return gof_ids

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]) -> List[str]:
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids

    @staticmethod
    def _get_stage_ids(
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO]
    ) -> List[int]:
        stage_ids = [
            stage_id_with_template_id_dto.stage_id
            for stage_id_with_template_id_dto in stage_id_with_template_id_dtos
        ]
        return stage_ids

    @staticmethod
    def _get_gof_ids_having_at_least_one_field(
            gof_ids: List[str],
            field_with_permissions_dtos: List[FieldPermissionDTO]) -> List[str]:
        field_dtos = [
            field_with_permissions_dto.field_dto
            for field_with_permissions_dto in field_with_permissions_dtos
        ]

        gof_ids_of_fields = [
            field_dto.gof_id for field_dto in field_dtos
        ]
        gof_ids_having_at_least_one_field = [
            gof_id for gof_id in gof_ids if gof_id in gof_ids_of_fields
        ]

        return gof_ids_having_at_least_one_field

    @staticmethod
    def _get_gof_details_with_user_permitted_gof_ids(
            gof_details_dicts: List[Dict],
            gof_ids_having_user_read_permissions: List[str]) -> List[Dict]:
        for gof_details_dict in gof_details_dicts:
            gof_ids = gof_details_dict["gof_ids"]
            gof_ids_of_gof_selector_having_user_read_permission = [
                gof_id for gof_id in gof_ids
                if gof_id in gof_ids_having_user_read_permissions
            ]
            is_user_has_no_read_permission_for_gof_ids = \
                not gof_ids_of_gof_selector_having_user_read_permission
            if is_user_has_no_read_permission_for_gof_ids:
                gof_details_dicts.remove(gof_details_dict)
                continue

            gof_details_dict["gof_ids"] = \
                gof_ids_of_gof_selector_having_user_read_permission
        return gof_details_dicts

    @staticmethod
    def _get_task_template_ids(task_templates_dtos: List[TemplateDTO]):
        task_templates_ids = [
            task_templates_dto.template_id
            for task_templates_dto in task_templates_dtos
        ]
        return task_templates_ids

    @staticmethod
    def _get_field_with_is_field_writable_dtos(
            field_dtos: List[FieldDTO],
            field_ids_having_write_permission_for_user: List[str]
    ) -> List[FieldPermissionDTO]:
        field_with_is_field_writable_dtos = []
        for field_dto in field_dtos:
            is_field_writable = field_dto.field_id in \
                                field_ids_having_write_permission_for_user
            field_with_is_field_writable_dto = FieldPermissionDTO(
                field_dto=field_dto, is_field_writable=is_field_writable)
            field_with_is_field_writable_dtos.append(
                field_with_is_field_writable_dto)
        return field_with_is_field_writable_dtos
