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
            self, project_id: str, user_id: str,
            presenter: GetGroupByPresenterInterface
    ):
        group_by_response_dtos = self.get_group_by(
            project_id=project_id, user_id=user_id
        )
        return presenter.get_response_for_get_group_by(
            group_by_response_dtos=group_by_response_dtos
        )

    def get_group_by(self, project_id: str, user_id: str):
        group_by_response_dtos = self.storage.get_group_by_dtos(user_id=user_id)
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
