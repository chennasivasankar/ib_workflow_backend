from typing import List, Dict

from ib_tasks.interactors.presenter_interfaces. \
    get_transition_template_presenter_interface import \
    GetTransitionTemplatePresenterInterface, CompleteTransitionTemplateDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_dtos import \
    GoFToTaskTemplateDTO
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
            return presenter. \
                raise_transition_template_does_not_exists_exception(err)

        transition_template_response_object = \
            presenter.get_transition_template_response(
                complete_transition_template_dto=
                complete_transition_template_dto
            )
        return transition_template_response_object

    def get_transition_template(
            self, user_id: str, transition_template_id: str
    ) -> CompleteTransitionTemplateDTO:

        self._validate_transition_template_id(
            transition_template_id=transition_template_id)

        transition_template_dto = \
            self.task_template_storage.get_transition_template_dto(
                transition_template_id=transition_template_id)

        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        service_adapter = get_roles_service_adapter()
        user_roles = \
            service_adapter.roles_service.get_user_role_ids(user_id=user_id)

        gofs_of_transition_template_dtos = \
            self._get_gofs_of_transition_template_permitted_for_user_dtos(
                transition_template_id=transition_template_id,
                user_roles=user_roles)

        gof_ids_of_transition_template = self._get_gof_ids(
            gofs_of_transition_template_dtos=gofs_of_transition_template_dtos)

        field_dtos = self._get_fields_of_gofs_in_dtos(
            gof_ids=gof_ids_of_transition_template, user_roles=user_roles)

        gof_ids_with_at_least_one_field = \
            self._get_gof_ids_having_at_least_one_field(
                gof_ids=gof_ids_of_transition_template, field_dtos=field_dtos)

        field_dtos = self.\
            _remove_gof_ids_from_gof_selector_if_user_having_no_read_permission(
                field_dtos=field_dtos,
                gof_ids_having_user_read_permissions=
                gof_ids_with_at_least_one_field
            )

        gofs_details_dtos = \
            self.gof_storage.get_gofs_details_dtos_for_given_gof_ids(
                gof_ids=gof_ids_with_at_least_one_field)

        gofs_of_transition_template_having_at_least_one_field_dtos = self.\
            _get_gofs_of_transition_template_having_at_least_one_field_dtos(
                gofs_of_transition_template_dtos=
                gofs_of_transition_template_dtos,
                gof_ids_with_at_least_one_field=gof_ids_with_at_least_one_field

            )

        return CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gofs_details_dtos,
            gofs_of_transition_template_dtos=
            gofs_of_transition_template_having_at_least_one_field_dtos,
            field_dtos=field_dtos)

    def _get_gofs_of_transition_template_permitted_for_user_dtos(
            self, user_roles: List[str], transition_template_id: str
    ) -> List[GoFToTaskTemplateDTO]:
        gof_ids_of_transition_template = \
            self.task_template_storage.get_gof_ids_of_template(
                template_id=transition_template_id
            )

        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        gof_ids_having_read_permission_for_user = \
            user_role_validation_interactor. \
            get_gof_ids_having_read_permission_for_user(
                user_roles=user_roles, gof_ids=gof_ids_of_transition_template,
                gof_storage=self.gof_storage)
        gofs_of_transition_template_permitted_for_user_dtos = \
            self.task_template_storage. \
            get_gofs_to_template_from_given_gofs(
                gof_ids=gof_ids_having_read_permission_for_user,
                template_id=transition_template_id
            )
        return gofs_of_transition_template_permitted_for_user_dtos

    def _validate_transition_template_id(self, transition_template_id: str):
        is_valid_transition_template_id = \
            self.task_template_storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)
        is_invalid_transition_template_id = not is_valid_transition_template_id

        from ib_tasks.exceptions.task_custom_exceptions import \
            TransitionTemplateDoesNotExist
        if is_invalid_transition_template_id:
            raise TransitionTemplateDoesNotExist(transition_template_id)

    def _get_fields_of_gofs_in_dtos(
            self, gof_ids: List[str], user_roles: List[str]) -> List[FieldDTO]:
        field_ids_of_gofs = self.field_storage.get_field_ids_for_given_gofs(
            gof_ids=gof_ids)

        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        field_ids_having_write_permission_for_user = \
            user_role_validation_interactor. \
            get_field_ids_having_write_permission_for_user(
                user_roles=user_roles, field_ids=field_ids_of_gofs,
                field_storage=self.field_storage)

        field_dtos = self.field_storage.get_field_dtos(
            field_ids=field_ids_having_write_permission_for_user)

        return field_dtos

    def _remove_gof_ids_from_gof_selector_if_user_having_no_read_permission(
            self, field_dtos: List[FieldDTO],
            gof_ids_having_user_read_permissions: List[str]) -> List[FieldDTO]:
        import json
        from ib_tasks.constants.enum import FieldTypes
        for field_dto in field_dtos:
            is_field_is_gof_selector = \
                field_dto.field_type == FieldTypes.GOF_SELECTOR.value
            if is_field_is_gof_selector:
                field_values = json.loads(field_dto.field_values)
                gof_details = self._get_gof_details_with_user_permitted_gof_ids(
                    gof_details_dicts=field_values,
                    gof_ids_having_user_read_permissions=
                    gof_ids_having_user_read_permissions
                )
                field_dto.field_values = json.dumps(gof_details)
        return field_dtos

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]) -> List[str]:
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids

    @staticmethod
    def _get_gof_ids(
            gofs_of_transition_template_dtos: List[GoFToTaskTemplateDTO]):
        gof_ids = [
            gofs_of_transition_template_dto.gof_id
            for gofs_of_transition_template_dto
            in gofs_of_transition_template_dtos
        ]
        return gof_ids

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
    def _get_gof_ids_having_at_least_one_field(
            gof_ids: List[str], field_dtos: List[FieldDTO]) -> List[str]:
        gof_ids_of_fields = [
            field_dto.gof_id for field_dto in field_dtos
        ]
        gof_ids_having_at_least_one_field = [
            gof_id for gof_id in gof_ids if gof_id in gof_ids_of_fields
        ]

        return gof_ids_having_at_least_one_field

    @staticmethod
    def _get_gofs_of_transition_template_having_at_least_one_field_dtos(
            gofs_of_transition_template_dtos: List[GoFToTaskTemplateDTO],
            gof_ids_with_at_least_one_field: List[str]
    ) -> List[GoFToTaskTemplateDTO]:
        gofs_of_transition_template_having_at_least_one_field_dtos = [
            gofs_of_transition_template_dto
            for gofs_of_transition_template_dto in
            gofs_of_transition_template_dtos
            if gofs_of_transition_template_dto.gof_id in
            gof_ids_with_at_least_one_field
        ]
        return gofs_of_transition_template_having_at_least_one_field_dtos
