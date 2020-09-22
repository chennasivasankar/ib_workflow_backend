from typing import List, Optional, Union

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds, \
    DuplicateSameGoFOrderForAGoF, InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsFieldWritablePermission
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
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import GoFFieldsDTO, FieldValuesDTO


class GoFsDetailsValidationsInteractor:

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

    def perform_gofs_details_validations(
            self, gof_fields_dtos: List[GoFFieldsDTO], user_id: str,
            task_template_id: str, project_id: str,
            action_type: Optional[ActionTypes], stage_id: int):
        gof_ids = self._validate_gof_details_and_get_gof_ids(gof_fields_dtos)
        field_ids = self._validate_fields(gof_fields_dtos)
        self._validate_that_fields_gofs_and_template_are_related(
            task_template_id, gof_ids, gof_fields_dtos, stage_id)
        self._validate_user_permission_on_given_fields(
            field_ids, user_id, project_id)
        self._validate_given_field_responses(gof_fields_dtos, action_type)

    def _validate_gof_details_and_get_gof_ids(
            self, gof_fields_dtos: List[GoFFieldsDTO]) -> List[str]:
        self._validate_same_gof_order(gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in gof_fields_dtos
        ]
        self._validate_for_invalid_gof_ids(gof_ids)
        return gof_ids

    def _validate_fields(
            self, gof_fields_dtos: List[GoFFieldsDTO]) -> List[str]:
        field_values_dtos = self._get_field_values_dtos(gof_fields_dtos)
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        self._validate_for_invalid_field_ids(field_ids)
        return field_ids

    def _validate_that_fields_gofs_and_template_are_related(
            self, task_template_id: str, gof_ids: List[str],
            gof_fields_dtos: List[GoFFieldsDTO], stage_id: int):
        self._validate_for_given_gofs_are_related_to_given_task_template(
            task_template_id, gof_ids)
        self._validate_for_given_fields_are_related_to_given_gofs(
            gof_fields_dtos, gof_ids)
        task_template_is_transition_template = \
            self.task_template_storage.check_is_transition_template_exists(
                task_template_id)
        if task_template_is_transition_template:
            return
        self._validate_stage_permitted_gofs(gof_ids, stage_id)

    def _validate_given_field_responses(
            self, gof_fields_dots: List[GoFFieldsDTO],
            action_type: ActionTypes):
        from ib_tasks.interactors.create_or_update_task. \
            validate_field_responses import ValidateFieldResponsesInteractor
        field_validation_interactor = ValidateFieldResponsesInteractor(
            self.field_storage)
        field_values_dtos = \
            self._get_field_values_dtos(gof_fields_dots)
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

    def _validate_user_permission_on_given_fields(
            self, field_ids: List[str], user_id: str, project_id: str
    ) -> Union[None, Exception]:
        from ib_tasks.constants.constants import ALL_ROLES_ID
        user_roles = self._get_user_roles_of_project(user_id, project_id)
        field_write_permission_roles_dtos = \
            self.field_storage.get_write_permission_roles_for_given_field_ids(
                field_ids)
        for field_roles_dto in field_write_permission_roles_dtos:
            required_roles = field_roles_dto.write_permission_roles
            required_roles_has_all_roles = ALL_ROLES_ID in required_roles
            if required_roles_has_all_roles:
                continue
            user_permitted = self.any_in(user_roles, required_roles)
            required_roles_are_empty = not required_roles
            if not user_permitted or required_roles_are_empty:
                raise UserNeedsFieldWritablePermission(
                    user_id, field_roles_dto.field_id, required_roles)
        return

    @staticmethod
    def _get_user_roles_of_project(
            user_id: str, project_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(user_id, project_id)
        return user_roles

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
            self, gof_ids: List[str]) -> Optional[InvalidGoFIds]:
        valid_gof_ids = self.gof_storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = sorted(list(set(gof_ids) - set(valid_gof_ids)))
        if invalid_gof_ids:
            raise InvalidGoFIds(invalid_gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, field_ids: List[str]) -> Optional[InvalidFieldIds]:
        valid_field_ids = self.task_storage.get_existing_field_ids(field_ids)
        invalid_field_ids = sorted(list(set(field_ids) - set(valid_field_ids)))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
        return

    def _validate_stage_permitted_gofs(
            self, gof_ids: List[str], stage_id: int
    ) -> Optional[InvalidStagePermittedGoFs]:
        permitted_gof_ids = \
            self.task_template_storage.get_stage_permitted_gof_ids(stage_id)
        not_permitted_gof_ids = list(
            sorted(set(gof_ids) - set(permitted_gof_ids)))
        if not_permitted_gof_ids:
            raise InvalidStagePermittedGoFs(not_permitted_gof_ids, stage_id)
        return