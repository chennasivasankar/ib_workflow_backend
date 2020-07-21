from typing import List
from ib_tasks.interactors.storage_interfaces.dtos \
    import FieldDTO, FieldRolesDTO, FieldRoleDTO

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface

from ib_tasks.constants.enum import PermissionTypes, FieldTypes

from ib_tasks.interactors.multi_values_input_fileds_validation_interactor \
    import MultiValuesInputFieldsValidationInteractor

from ib_tasks.interactors.gof_selector_validations_interactor \
    import GoFSelectorValidationsInteractor


class CreateOrUpdateFieldsInteractor:

    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def create_or_update_fields(
            self, field_dtos: List[FieldDTO],
            field_roles_dtos: List[FieldRolesDTO]
    ):
        self._check_for_base_validations(field_dtos)
        self._check_for_field_roles_validations(field_roles_dtos)
        self._vlidate_field_values_based_on_field_types(field_dtos)
        field_role_dtos = self._get_field_role_dtos(field_roles_dtos)

        new_field_dtos, existing_field_dtos = self._get_field_dtos(field_dtos)
        new_field_role_dtos, existing_field_role_dtos = \
            self._get_new_and_exist_field_role_dtos(field_role_dtos)

        if new_field_dtos:
            self.storage.create_fields(new_field_dtos)
            self.storage.create_fields_roles(new_field_role_dtos)
        if existing_field_dtos:
            self.storage.update_fields(existing_field_dtos)
            self.storage.update_fields_roles(existing_field_role_dtos)

    def _check_for_base_validations(self, field_dtos: List[FieldDTO]):

        from ib_tasks.interactors.create_or_update_fields_base_validations_interactor \
            import CreateOrUpdateFieldsBaseVaidationInteractor
        base_validation_interactor = \
            CreateOrUpdateFieldsBaseVaidationInteractor(storage=self.storage)
        base_validation_interactor.fields_base_validations(field_dtos)

    def _check_for_field_roles_validations(
            self, field_roles_dtos: List[FieldRolesDTO]
    ):
        from ib_tasks.interactors.fields_roles_validations_interactor \
            import FieldsRolesValidationsInteractor

        field_roles_validation_interactor = FieldsRolesValidationsInteractor()
        field_roles_validation_interactor.fields_roles_validations(field_roles_dtos)

    def _vlidate_field_values_based_on_field_types(self, field_dtos: List[FieldDTO]):
        for field_dto in field_dtos:
            self._validate_field_value(field_dto)

    def _get_field_role_dtos(self, field_roles_dtos: List[FieldRolesDTO]):
        field_role_dtos = []
        for field_roles_dto in field_roles_dtos:
            read_permission_field_role_dtos = \
                self._get_read_permission_field_role_dtos(field_roles_dto)
            write_permission_field_role_dtos = \
                self._get_write_permission_field_role_dtos(field_roles_dto)
            field_role_dtos = (
                    field_role_dtos +
                    read_permission_field_role_dtos +
                    write_permission_field_role_dtos
            )
        return field_role_dtos

    def _get_read_permission_field_role_dtos(
            self, field_roles_dto: FieldRolesDTO
    ) -> List[FieldRoleDTO]:

        read_permission_field_role_dtos = []
        field_id = field_roles_dto.field_id
        read_permission_roles = field_roles_dto.read_permission_roles
        for role in read_permission_roles:
            field_role_dto = FieldRoleDTO(
                field_id=field_id, role=role,
                permission_type=PermissionTypes.READ.value
            )
            read_permission_field_role_dtos.append(field_role_dto)
        return read_permission_field_role_dtos

    def _get_write_permission_field_role_dtos(
            self, field_roles_dto: FieldRolesDTO
    ) -> List[FieldRoleDTO]:

        write_permission_field_role_dtos = []
        field_id = field_roles_dto.field_id
        write_permission_roles = field_roles_dto.write_permission_roles
        for role in write_permission_roles:
            field_role_dto = FieldRoleDTO(
                field_id=field_id, role=role,
                permission_type=PermissionTypes.WRITE.value
            )
            write_permission_field_role_dtos.append(field_role_dto)
        return write_permission_field_role_dtos

    def _get_field_dtos(self, field_dtos: List[FieldDTO]):
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        existing_field_ids = self.storage.get_existing_field_ids(field_ids)
        new_field_ids = [
            field_id
            for field_id in field_ids
            if field_id not in existing_field_ids
        ]
        new_field_dtos = [
            field_dto
            for field_dto in field_dtos
            if field_dto.field_id in new_field_ids
        ]
        existing_field_dtos = [
            field_dto
            for field_dto in field_dtos
            if field_dto.field_id in existing_field_ids
        ]
        return new_field_dtos, existing_field_dtos

    def _get_new_and_exist_field_role_dtos(self, field_role_dtos: List[FieldRoleDTO]):
        field_ids = [field_role_dto.field_id for field_role_dto in field_role_dtos]
        existing_field_role_dtos = self.storage.get_fields_role_dtos(field_ids)
        new_role_dtos = []
        for field_role_dto in field_role_dtos:
            is_new_role_dto = self._is_field_role_dto_matches(
                field_role_dto, existing_field_role_dtos
            )
            if is_new_role_dto:
                new_role_dtos.append(field_role_dto)
        return new_role_dtos, existing_field_role_dtos

    def _is_field_role_dto_matches(
            self, field_role_dto: FieldRoleDTO,
            field_role_dtos: List[FieldRoleDTO]
    ):
        field_id = field_role_dto.field_id
        role = field_role_dto.role
        for role_dto in field_role_dtos:
            exist_field_id, exist_role = role_dto.field_id, role_dto.role
            is_field_role_matches = field_id == exist_field_id and role == exist_role
            if is_field_role_matches:
                return False
        return True

    def _validate_field_value(self, field_dto: FieldDTO):
        from ib_tasks.constants.constants import MULTI_VALUES_INPUT_FIELDS
        field_type = field_dto.field_type
        if field_type in MULTI_VALUES_INPUT_FIELDS:
            interactor = MultiValuesInputFieldsValidationInteractor()
            interactor.multi_values_input_fields_validations(field_dto)
        if field_type == FieldTypes.GOF_SELECTOR.value:
            interactor = GoFSelectorValidationsInteractor(storage=self.storage)
            interactor.gof_selecter_validations(field_dto)