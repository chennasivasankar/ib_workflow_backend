from typing import List, Dict

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.presenter_interfaces. \
    get_transition_template_presenter_interface import \
    GetTransitionTemplatePresenterInterface, CompleteTransitionTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    UserFieldPermissionDTO, FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class GetTransitionTemplateInteractor:
    def __init__(
            self, task_storage: TaskStorageInterface,
            task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface,
            field_storage: FieldsStorageInterface,
    ):
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage

    def get_transition_template_wrapper(
            self, user_id: str, transition_template_id: str,
            presenter: GetTransitionTemplatePresenterInterface):

        from ib_tasks.exceptions.task_custom_exceptions import \
            TransitionTemplateDoesNotExist
        try:
            complete_transition_template_dto = self.get_transition_template(
                user_id=user_id, transition_template_id=transition_template_id
            )
        except TransitionTemplateDoesNotExist as err:
            return presenter.\
                raise_transition_template_does_not_exists_exception(err)

        transition_template_response_object = \
            presenter.get_transition_template_response(
                complete_transition_template_dto=complete_transition_template_dto
            )
        return transition_template_response_object

    def get_transition_template(
            self, user_id: str, transition_template_id: str
    ) -> CompleteTransitionTemplateDTO:

        self._validate_transition_template_id(
            transition_template_id=transition_template_id)
        user_roles = self._get_user_role_ids(user_id=user_id)

        transition_template_dto = \
            self.task_template_storage.get_transition_template_dto(
                transition_template_id=transition_template_id)
        gof_ids_permitted_for_user = \
            self.gof_storage.get_gof_ids_with_read_permission_for_user(
                roles=user_roles)
        gofs_of_transition_template_dtos = self.task_template_storage. \
            get_gofs_to_template_from_permitted_gofs(
                gof_ids=gof_ids_permitted_for_user,
                template_id=transition_template_id
            )
        gofs_details_dtos = \
            self.gof_storage.get_gofs_details_dtos_for_given_gof_ids(
                gof_ids=gof_ids_permitted_for_user)
        field_with_permissions_dtos = \
            self._get_field_with_permissions_of_gofs_in_dtos(
                gof_ids=gof_ids_permitted_for_user, user_roles=user_roles)

        return CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gofs_details_dtos,
            gofs_of_transition_template_dtos=gofs_of_transition_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

    def _validate_transition_template_id(self, transition_template_id: str):
        is_valid_transition_template_id = \
            self.task_template_storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)
        is_invalid_transition_template_id = not is_valid_transition_template_id

        from ib_tasks.exceptions.task_custom_exceptions import \
            TransitionTemplateDoesNotExist
        if is_invalid_transition_template_id:
            raise TransitionTemplateDoesNotExist(transition_template_id)

    def _get_field_with_permissions_of_gofs_in_dtos(
            self, gof_ids: List[str],
            user_roles: List[str]) -> List[FieldPermissionDTO]:
        field_dtos = \
            self.field_storage.get_fields_of_gofs_in_dtos(gof_ids=gof_ids)
        field_ids = self._get_field_ids(field_dtos=field_dtos)
        user_field_permission_dtos = self.field_storage. \
            get_user_field_permission_dtos(
                roles=user_roles, field_ids=field_ids
            )
        user_field_permission_dtos_dict = \
            self._make_user_field_permission_dtos_dict(
                user_field_permission_dtos=user_field_permission_dtos
            )

        field_permission_dtos = []
        for field_dto in field_dtos:
            if field_dto.field_id in user_field_permission_dtos_dict.keys():
                permission_type = \
                    user_field_permission_dtos_dict[
                        field_dto.field_id].permission_type
                field_permission_dto = \
                    self._get_field_with_permissions_dto(
                        field_dto=field_dto,
                        permission_type=permission_type
                    )
                field_permission_dtos.append(field_permission_dto)
        return field_permission_dtos

    @staticmethod
    def _get_field_with_permissions_dto(
            field_dto: FieldDTO,
            permission_type: PermissionTypes) -> FieldPermissionDTO:
        has_write_permission = permission_type == PermissionTypes.WRITE.value
        is_field_writable = False
        if has_write_permission:
            is_field_writable = True

        field_permission_dto = FieldPermissionDTO(
            field_dto=field_dto,
            is_field_writable=is_field_writable
        )
        return field_permission_dto

    @staticmethod
    def _make_user_field_permission_dtos_dict(
            user_field_permission_dtos: List[UserFieldPermissionDTO]) -> Dict:
        import collections
        user_permission_dtos_dict = collections.defaultdict()

        for user_field_permission_dto in user_field_permission_dtos:
            user_permission_dtos_dict[user_field_permission_dto.field_id] = \
                user_field_permission_dto

        return user_permission_dtos_dict

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]) -> List[str]:
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        user_roles = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)
        return user_roles
