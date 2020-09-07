from typing import List, Optional, Union

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF, UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds, \
    DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface\
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import GoFFieldsDTO, FieldValuesDTO


class TemplateGoFsFieldsBaseValidationsInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface,
            task_template_storage: TaskTemplateStorageInterface
    ):
        self.gof_storage = gof_storage
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage
        self.task_template_storage = task_template_storage

    def perform_base_validations_for_template_gofs_and_fields(
            self, gof_fields_dtos: List[GoFFieldsDTO], user_id: str,
            task_template_id: str, project_id: str,
            action_type: Optional[ActionTypes]):
        self._validate_same_gof_order(gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in gof_fields_dtos
        ]
        field_values_dtos = self._get_field_values_dtos(gof_fields_dtos)
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        self._validate_for_invalid_gof_ids(gof_ids)
        self._validate_for_invalid_field_ids(field_ids)
        self._validate_for_given_gofs_are_related_to_given_task_template(
            task_template_id, gof_ids)
        self._validate_for_given_fields_are_related_to_given_gofs(
            gof_fields_dtos, gof_ids)
        self._validate_user_permission_on_given_fields_and_gofs(
            gof_ids, field_ids, user_id)
        self._validate_all_user_template_permitted_fields_are_filled_or_not(
            user_id=user_id, project_id=project_id,
            task_template_id=task_template_id, gof_fields_dtos=gof_fields_dtos
        )
        from ib_tasks.interactors.create_or_update_task. \
            validate_field_responses import ValidateFieldResponsesInteractor
        field_validation_interactor = ValidateFieldResponsesInteractor(
            self.field_storage)
        field_values_dtos = \
            self._get_field_values_dtos(gof_fields_dtos)
        field_validation_interactor.validate_field_responses(
            field_values_dtos, action_type)

    def _validate_same_gof_order(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[DuplicateSameGoFOrderForAGoF]:
        from collections import defaultdict
        gof_with_order_dict = defaultdict(list)
        for gof_fields_dto in gof_fields_dtos:
            gof_with_order_dict[
                gof_fields_dto.gof_id].append(gof_fields_dto.same_gof_order)
        for gof_id, same_gof_orders in gof_with_order_dict.items():
            duplicate_same_gof_orders = self._get_duplicates_in_given_list(
                same_gof_orders)
            if duplicate_same_gof_orders:
                raise DuplicateSameGoFOrderForAGoF(gof_id,
                                                   duplicate_same_gof_orders)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List) -> List:
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        duplicate_values.sort()
        return duplicate_values

    def _validate_user_permission_on_given_fields_and_gofs(
            self, gof_ids: List[str], field_ids: List[str], user_id: str
    ) -> Union[None, UserNeedsGoFWritablePermission,
               UserNeedsFieldWritablePermission]:
        gof_write_permission_roles_dtos = \
            self.storage.get_write_permission_roles_for_given_gof_ids(gof_ids)
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service.get_user_role_ids(
            user_id)
        for gof_roles_dto in gof_write_permission_roles_dtos:
            required_roles = gof_roles_dto.write_permission_roles
            from ib_tasks.constants.constants import ALL_ROLES_ID
            required_roles_has_all_roles = ALL_ROLES_ID in required_roles
            if required_roles_has_all_roles:
                continue
            user_permitted = self.any_in(user_roles, required_roles)
            required_roles_are_empty = not required_roles
            if not user_permitted or required_roles_are_empty:
                raise UserNeedsGoFWritablePermission(user_id,
                                                     gof_roles_dto.gof_id,
                                                     required_roles)
        field_write_permission_roles_dtos = \
            self.storage.get_write_permission_roles_for_given_field_ids(
                field_ids)
        for field_roles_dto in field_write_permission_roles_dtos:
            required_roles = field_roles_dto.write_permission_roles
            from ib_tasks.constants.constants import ALL_ROLES_ID
            required_roles_has_all_roles = ALL_ROLES_ID in required_roles
            if required_roles_has_all_roles:
                continue
            user_permitted = self.any_in(user_roles, required_roles)
            required_roles_are_empty = not required_roles
            if not user_permitted or required_roles_are_empty:
                raise UserNeedsFieldWritablePermission(user_id,
                                                       field_roles_dto.field_id,
                                                       required_roles)
        return

    @staticmethod
    def any_in(user_roles: List[str], required_roles: List[str]) -> bool:
        from ib_iam.constants.config import ALL_ROLES_ID
        return any(role in required_roles for role in
                   user_roles) or ALL_ROLES_ID in required_roles

    def _validate_for_given_fields_are_related_to_given_gofs(
            self, gof_fields_dtos: List[GoFFieldsDTO], gof_ids: List[str]
    ) -> Union[None, InvalidFieldsOfGoF, DuplicateFieldIdsToGoF]:
        from collections import defaultdict
        field_id_with_gof_id_dtos = \
            self.field_storage.get_field_ids_related_to_given_gof_ids(gof_ids)
        gof_fields_dict = defaultdict(list)
        for field_id_with_gof_id_dto in field_id_with_gof_id_dtos:
            gof_fields_dict[field_id_with_gof_id_dto.gof_id] \
                .append(field_id_with_gof_id_dto.field_id)
        for gof_fields_dto in gof_fields_dtos:
            given_gof_field_ids = [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
            valid_gof_field_ids = gof_fields_dict[gof_fields_dto.gof_id]
            self._validate_for_invalid_fields_to_given_gof(
                gof_fields_dto.gof_id, given_gof_field_ids, valid_gof_field_ids
            )
        return

    def _validate_for_invalid_fields_to_given_gof(
            self, gof_id: str, given_gof_field_ids: List[str],
            valid_gof_field_ids: List[str]
    ) -> Union[None, InvalidFieldsOfGoF, DuplicateFieldIdsToGoF]:
        duplicate_field_ids = self._get_duplicates_in_given_list(
            given_gof_field_ids)
        if duplicate_field_ids:
            raise DuplicateFieldIdsToGoF(gof_id, duplicate_field_ids)
        invalid_gof_field_ids = sorted(list(
            set(given_gof_field_ids) - set(valid_gof_field_ids)
        ))
        if invalid_gof_field_ids:
            raise InvalidFieldsOfGoF(gof_id, invalid_gof_field_ids)
        return

    def _validate_for_given_gofs_are_related_to_given_task_template(
            self, task_template_id: str, gof_ids: List[str]
    ) -> Optional[InvalidGoFsOfTaskTemplate]:
        valid_task_template_gof_ids = self.create_task_storage. \
            get_all_gof_ids_related_to_a_task_template(task_template_id)
        invalid_task_template_gof_ids = sorted(list(
            set(gof_ids) - set(valid_task_template_gof_ids)))
        if invalid_task_template_gof_ids:
            raise InvalidGoFsOfTaskTemplate(
                invalid_task_template_gof_ids, task_template_id)
        return

    @staticmethod
    def _get_field_values_dtos(
            gof_fields_dtos: List[GoFFieldsDTO]
    ) -> List[FieldValuesDTO]:
        field_values_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            field_values_dtos += [
                field_value_dto
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        return field_values_dtos

    def _validate_for_invalid_gof_ids(
            self, gof_ids: List[str]
    ) -> Optional[InvalidGoFIds]:
        valid_gof_ids = self.gof_storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = sorted(list(set(gof_ids) - set(valid_gof_ids)))
        if invalid_gof_ids:
            raise InvalidGoFIds(invalid_gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, field_ids: List[str]
    ) -> Optional[InvalidFieldIds]:
        valid_field_ids = self.task_storage.get_existing_field_ids(field_ids)
        invalid_field_ids = sorted(list(set(field_ids) - set(valid_field_ids)))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List) -> List:
        duplicate_values = sorted(list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        ))
        return duplicate_values

    def _validate_all_user_template_permitted_fields_are_filled_or_not(
            self, user_id: str, project_id: str, task_template_id: str,
            gof_fields_dtos: List[GoFFieldsDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        template_gof_ids = self.task_template_storage.get_gof_ids_of_template(
            template_id=task_template_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, template_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        field_id_with_display_name_dtos = \
            self.field_storage \
                .get_user_write_permitted_field_ids_for_given_gof_ids(
                user_roles, user_permitted_gof_ids)
        filled_gof_ids = [
            gof_field_dto.gof_id for gof_field_dto in gof_fields_dtos]
        filled_field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            filled_field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        self._validate_all_user_permitted_gof_ids_are_filled_or_not(
            gof_id_with_display_name_dtos, filled_gof_ids)
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

    @staticmethod
    def _validate_all_user_permitted_gof_ids_are_filled_or_not(
            permitted_gofs, filled_gof_ids
    ) -> Optional[UserDidNotFillRequiredGoFs]:
        permitted_gof_ids = [
            permitted_gof.gof_id for permitted_gof in permitted_gofs]
        unfilled_gof_ids = list(sorted(
            set(permitted_gof_ids) - set(filled_gof_ids)))
        if unfilled_gof_ids:
            gof_display_names = [
                permitted_gof.gof_display_name
                for permitted_gof in permitted_gofs
                if permitted_gof.gof_id in unfilled_gof_ids
            ]
            raise UserDidNotFillRequiredGoFs(gof_display_names)
        return

    @staticmethod
    def _validate_all_user_permitted_field_ids_are_filled_or_not(
            permitted_fields, filled_field_ids
    ) -> Optional[UserDidNotFillRequiredFields]:
        permitted_field_ids = [
            permitted_field.field_id for permitted_field in permitted_fields]
        unfilled_field_ids = list(sorted(
            set(permitted_field_ids) - set(filled_field_ids)))
        if unfilled_field_ids:
            unfilled_field_dtos = [
                permitted_field
                for permitted_field in permitted_fields
                if permitted_field.field_id in unfilled_field_ids
            ]
            raise UserDidNotFillRequiredFields(unfilled_field_dtos)
        return
