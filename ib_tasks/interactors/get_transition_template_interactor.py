from typing import List

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
            return presenter.\
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

        gofs_of_transition_template_dtos = \
            self._get_gofs_of_transition_template_permitted_for_user_dtos(
                transition_template_id=transition_template_id,
                user_id=user_id)

        gof_ids_of_transition_template = self._get_gof_ids(
            gofs_of_transition_template_dtos=gofs_of_transition_template_dtos)
        gofs_details_dtos = \
            self.gof_storage.get_gofs_details_dtos_for_given_gof_ids(
                gof_ids=gof_ids_of_transition_template)

        field_dtos = self._get_fields_of_gofs_in_dtos(
            gof_ids=gof_ids_of_transition_template, user_id=user_id)

        return CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gofs_details_dtos,
            gofs_of_transition_template_dtos=gofs_of_transition_template_dtos,
            field_dtos=field_dtos)

    def _get_gofs_of_transition_template_permitted_for_user_dtos(
            self, user_id: str, transition_template_id: str
    ) -> List[GoFToTaskTemplateDTO]:
        gof_ids_of_transition_template = \
            self.task_template_storage.get_gof_ids_of_template(
                template_id=transition_template_id
            )

        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        gof_ids_having_read_permission_for_user = \
            user_role_validation_interactor.\
            get_gof_ids_having_read_permission_for_user(
                user_id=user_id, gof_ids=gof_ids_of_transition_template,
                gof_storage=self.gof_storage
            )
        gofs_of_transition_template_permitted_for_user_dtos = \
            self.task_template_storage.\
            get_gofs_to_template_from_permitted_gofs(
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
            self, gof_ids: List[str], user_id: str) -> List[FieldDTO]:
        field_ids_of_gofs = self.field_storage.get_field_ids_for_given_gofs(
            gof_ids=gof_ids)

        from ib_tasks.interactors.user_role_validation_interactor import \
            UserRoleValidationInteractor
        user_role_validation_interactor = UserRoleValidationInteractor()
        field_ids_having_write_permission_for_user = \
            user_role_validation_interactor.\
            get_field_ids_having_write_permission_for_user(
                user_id=user_id, field_ids=field_ids_of_gofs,
                field_storage=self.field_storage)

        field_dtos = self.field_storage.get_field_dtos(
            field_ids=field_ids_having_write_permission_for_user)

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
