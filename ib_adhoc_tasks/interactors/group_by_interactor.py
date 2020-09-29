from typing import List

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.exceptions.custom_exceptions import \
    UserNotAllowedToCreateMoreThanOneGroupByInListView, \
    UserNotAllowedToCreateMoreThanTwoGroupByInKanbanView, \
    InvalidNumberOfGroupByKeysForListView, \
    InvalidNumberOfGroupByKeysForKanbanView
from ib_adhoc_tasks.interactors.dtos.dtos import GroupBYKeyDTO, \
    GroupByParameter
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
        return presenter.get_response_for_get_group_by(
            group_by_response_dtos=group_by_response_dtos
        )

    def get_group_by(self, project_id: str, user_id: str, view_type: ViewType):
        group_by_response_dtos = self.storage.get_group_by_dtos(
            user_id=user_id, view_type=view_type
        )
        group_by_parameter_dto = GroupByParameter(
            user_id=user_id,
            project_id=project_id,
            view_type=view_type
        )
        from ib_adhoc_tasks.constants.constants import group_by_types_list
        for group_by_response_dto in group_by_response_dtos:
            if group_by_response_dto.group_by_key not in group_by_types_list:
                group_by_response_dto.display_name = self._get_field_display_name(
                    group_by_parameter=group_by_parameter_dto,
                    field_id=group_by_response_dto.group_by_key
                )
        group_by_response_dtos.sort(key=lambda x: x.order)
        return group_by_response_dtos

    def add_or_edit_group_by_wrapper(
            self,
            group_by_key_dtos: List[GroupBYKeyDTO],
            group_by_parameter: GroupByParameter,
            presenter: AddOrEditGroupByPresenterInterface
    ):
        try:
            group_by_response_dtos = self.add_or_edit_group_by(
                group_by_key_dtos=group_by_key_dtos,
                group_by_parameter=group_by_parameter
            )
            return presenter.get_response_for_add_or_edit_group_by(
                group_by_response_dtos=group_by_response_dtos
            )
        except UserNotAllowedToCreateMoreThanOneGroupByInListView:
            return presenter.get_response_for_user_not_allowed_to_create_more_than_one_group_by_in_list_view()
        except UserNotAllowedToCreateMoreThanTwoGroupByInKanbanView:
            return presenter.get_response_for_user_not_allowed_to_create_more_than_two_group_by_in_kanban_view()

    def add_or_edit_group_by(
            self,
            group_by_key_dtos: List[GroupBYKeyDTO],
            group_by_parameter: GroupByParameter
    ):
        is_list_view = group_by_parameter.view_type == ViewType.LIST.value
        group_by_response_dtos = None
        if is_list_view:
            group_by_response_dtos = self._add_or_edit_group_by_for_list_view(
                group_by_key_dtos=group_by_key_dtos,
                group_by_parameter=group_by_parameter
            )
        else:
            group_by_response_dtos = self._add_or_edit_group_by_for_kanban_view(
                group_by_key_dtos=group_by_key_dtos,
                group_by_parameter=group_by_parameter
            )
        from ib_adhoc_tasks.constants.constants import group_by_types_list
        for group_by_response_dto in group_by_response_dtos:
            if group_by_response_dto.group_by_key not in group_by_types_list:
                group_by_response_dto.display_name = \
                    self._get_field_display_name(
                        group_by_parameter=group_by_parameter,
                        field_id=group_by_response_dto.group_by_key
                    )
        group_by_response_dtos.sort(key=lambda x: x.order)
        return group_by_response_dtos

    def _add_or_edit_group_by_for_list_view(
            self, group_by_key_dtos: List[GroupBYKeyDTO],
            group_by_parameter: GroupByParameter
    ):
        self._validate_is_list_view_creation_or_updation_is_possible(
            group_by_key_dtos=group_by_key_dtos
        )
        is_group_by_key_dtos_empty = not group_by_key_dtos
        group_by_response_dtos = None
        if is_group_by_key_dtos_empty:
            group_by_response_dtos, group_by_key_dtos = self._get_existing_group_by_key_dtos_for_list_view(
                user_id=group_by_parameter.user_id, view_type=group_by_parameter.view_type
            )
        if group_by_response_dtos:
            return group_by_response_dtos
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTO(
            user_id=group_by_parameter.user_id,
            view_type=group_by_parameter.view_type,
            group_by_key=group_by_key_dtos[0].group_by_key,
            order=group_by_key_dtos[0].order,
        )
        group_by_response_dto = self.storage.add_or_edit_group_by_for_list_view(
            add_or_edit_group_by_parameter_dto=
            add_or_edit_group_by_parameter_dto
        )
        return [group_by_response_dto]

    def _add_or_edit_group_by_for_kanban_view(
            self,
            group_by_key_dtos: List[GroupBYKeyDTO],
            group_by_parameter: GroupByParameter
    ):
        self._validate_is_kanban_view_creation_or_updation_is_possible(
            group_by_key_dtos=group_by_key_dtos
        )
        group_by_response_dtos = None
        is_group_by_key_dtos_empty = not group_by_key_dtos
        if is_group_by_key_dtos_empty:
            group_by_response_dtos, group_by_key_dtos = \
                self._get_existing_group_by_key_dto_for_kanban_view(
                    user_id=group_by_parameter.user_id,
                    view_type=group_by_parameter.view_type
                )
        if group_by_response_dtos:
            return sorted(group_by_response_dtos, key=lambda x: x.order)
        self.storage.delete_all_user_group_by(
            user_id=group_by_parameter.user_id, view_type=group_by_parameter.view_type
        )
        group_by_response_dtos = \
            self.storage.add_group_by_for_kanban_view_in_bulk(
                group_by_parameter=group_by_parameter,
                group_by_key_dtos=group_by_key_dtos
            )
        return sorted(group_by_response_dtos, key=lambda x: x.order)

    @staticmethod
    def _validate_is_list_view_creation_or_updation_is_possible(
            group_by_key_dtos: List[GroupBYKeyDTO]
    ):
        length_of_group_by_keys = len(group_by_key_dtos)
        is_not_creation_or_updation_possible = length_of_group_by_keys > 1
        if is_not_creation_or_updation_possible:
            raise InvalidNumberOfGroupByKeysForListView

    @staticmethod
    def _validate_is_kanban_view_creation_or_updation_is_possible(
            group_by_key_dtos: List[GroupBYKeyDTO]
    ):
        length_of_group_by_keys = len(group_by_key_dtos)
        is_creation_or_updation_possible = (
                length_of_group_by_keys == 0 or length_of_group_by_keys == 2
        )
        is_not_creation_or_updation_possible = not is_creation_or_updation_possible
        if is_not_creation_or_updation_possible:
            raise InvalidNumberOfGroupByKeysForKanbanView

    @staticmethod
    def _get_field_display_name(
            group_by_parameter: GroupByParameter, field_id: str
    ) -> str:
        from ib_adhoc_tasks.adapters.service_adapter import \
            get_service_adapter
        service = get_service_adapter()
        field_display_name = service.task_service.get_field_display_name(
            project_id=group_by_parameter.project_id,
            user_id=group_by_parameter.user_id,
            field_id=field_id
        )
        return field_display_name

    def _get_existing_group_by_key_dtos_for_list_view(self, user_id: str, view_type: ViewType):
        from ib_adhoc_tasks.constants.constants import GROUP_BY_KEY_1
        group_by_response_dtos = \
            self.storage.get_group_by_dtos(
                user_id=user_id, view_type=view_type
            )
        group_by_key_dtos = [
            GroupBYKeyDTO(group_by_key=GROUP_BY_KEY_1, order=1)
        ]
        return group_by_response_dtos, group_by_key_dtos

    def _get_existing_group_by_key_dto_for_kanban_view(self, user_id: str, view_type: ViewType):
        from ib_adhoc_tasks.constants.constants import \
            GROUP_BY_KEY_1, GROUP_BY_KEY_2
        group_by_response_dtos = \
            self.storage.get_group_by_dtos(
                user_id=user_id, view_type=view_type
            )
        group_by_key_dtos = [
            GroupBYKeyDTO(group_by_key=GROUP_BY_KEY_1, order=1),
            GroupBYKeyDTO(group_by_key=GROUP_BY_KEY_2, order=2)
        ]
        return group_by_response_dtos, group_by_key_dtos
