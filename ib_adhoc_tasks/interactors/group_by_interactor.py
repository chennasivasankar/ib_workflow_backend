from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.presenter_interfaces \
    .group_by_presenter_interface import GetGroupByPresenterInterface, \
    AddOrEditGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    AddOrEditGroupByParameterDTO
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GroupByInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_group_by_wrapper(
            self, project_id: str, user_id: str, view_type: ViewType,
            presenter: GetGroupByPresenterInterface
    ):
        group_by_response_dtos = self.get_group_by(
            project_id=project_id, user_id=user_id, view_type=view_type
        )
        from ib_adhoc_tasks.constants.constants import group_by_types_list
        for group_by_response_dto in group_by_response_dtos:
            if group_by_response_dto.group_by_key not in group_by_types_list:
                group_by_response_dto.display_name = \
                    self._get_field_display_name(
                        project_id=project_id, user_id=user_id,
                        field_id=group_by_response_dto.group_by_key
                    )
        return presenter.get_response_for_get_group_by(
            group_by_response_dtos=group_by_response_dtos
        )

    def get_group_by(self, project_id: str, user_id: str, view_type: ViewType):
        group_by_response_dtos = self.storage.get_group_by_dtos(
            user_id=user_id, view_type=view_type
        )
        group_by_response_dtos.sort(key=lambda x: x.order)
        return group_by_response_dtos

    def add_or_edit_group_by_wrapper(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO,
            presenter: AddOrEditGroupByPresenterInterface
    ):
        group_by_response_dto = self.add_or_edit_group_by(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )
        return presenter.get_response_for_add_or_edit_group_by(
            group_by_response_dto=group_by_response_dto
        )

    def add_or_edit_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ):
        is_group_by_id_exists = \
            add_or_edit_group_by_parameter_dto.group_by_id is not None
        if is_group_by_id_exists:
            group_by_response_dto = self.storage.edit_group_by(
                add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
            )
        else:
            group_by_response_dto = self.add_group_by(
                add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
            )
        from ib_adhoc_tasks.constants.constants import group_by_types_list
        if group_by_response_dto.group_by_key not in group_by_types_list:
            group_by_response_dto.display_name = \
                self._get_field_display_name(
                    project_id=add_or_edit_group_by_parameter_dto.project_id,
                    user_id=add_or_edit_group_by_parameter_dto.user_id,
                    field_id=group_by_response_dto.group_by_key
                )
        return group_by_response_dto

    def add_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ):
        from ib_adhoc_tasks.constants.enum import ViewType
        if add_or_edit_group_by_parameter_dto.view_type == ViewType.LIST.value:
            add_or_edit_group_by_parameter_dto.order = 1
        group_by_response_dto = self.storage.add_group_by(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )
        return group_by_response_dto

    @staticmethod
    def _get_field_display_name(
            project_id: str, user_id: str, field_id: str
    ) -> str:
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        field_display_name = service.task_service.get_field_display_name(
            project_id=project_id, user_id=user_id, field_id=field_id
        )
        return field_display_name
