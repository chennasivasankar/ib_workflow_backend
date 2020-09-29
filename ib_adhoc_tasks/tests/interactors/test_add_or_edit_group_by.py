import mock
import pytest

from ib_adhoc_tasks.constants.enum import ViewType, GroupByKey
from ib_adhoc_tasks.tests.factories.interactor_dtos import \
    GroupByParameterFactory, GroupBYKeyDTOFactory
from ib_adhoc_tasks.tests.factories.storage_dtos import \
    AddOrEditGroupByParameterDTOFactory, GroupByResponseDTOFactory


class TestGetGroupByInteractor:

    @pytest.fixture
    def storage(self):
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .storage_interface import StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.interactors.presenter_interfaces.group_by_presenter_interface import \
            AddOrEditGroupByPresenterInterface
        return mock.create_autospec(AddOrEditGroupByPresenterInterface)

    @pytest.fixture
    def interactor(self, storage):
        from ib_adhoc_tasks.interactors.group_by_interactor import \
            GroupByInteractor
        return GroupByInteractor(storage=storage)

    @pytest.fixture
    def get_dtos_for_add_group_by_for_list(self):
        GroupByParameterFactory.reset_sequence(0)
        GroupByParameterFactory.view_type.reset()
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupBYKeyDTOFactory.group_by_key.reset()
        GroupBYKeyDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        GroupByResponseDTOFactory.order.reset()
        AddOrEditGroupByParameterDTOFactory.reset_sequence(0)
        AddOrEditGroupByParameterDTOFactory.group_by_key.reset()
        AddOrEditGroupByParameterDTOFactory.order.reset()
        AddOrEditGroupByParameterDTOFactory.view_type.reset()
        group_by_parameter = GroupByParameterFactory(
            view_type=ViewType.LIST.value)
        group_by_key_dtos = [GroupBYKeyDTOFactory()]
        group_by_response_dtos = [GroupByResponseDTOFactory()]
        add_or_edit_group_by_parameter_dto = \
            AddOrEditGroupByParameterDTOFactory()
        return {
            "group_by_parameter": group_by_parameter,
            "group_by_key_dtos": group_by_key_dtos,
            "group_by_response_dtos": group_by_response_dtos,
            "add_or_edit_group_by_parameter_dto":
                add_or_edit_group_by_parameter_dto
        }

    @pytest.fixture
    def get_dtos_for_add_group_by_for_kanban(self):
        GroupByParameterFactory.reset_sequence(0)
        GroupByParameterFactory.view_type.reset()
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupBYKeyDTOFactory.group_by_key.reset()
        GroupBYKeyDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        GroupByResponseDTOFactory.order.reset()
        AddOrEditGroupByParameterDTOFactory.reset_sequence(0)
        group_by_parameter = GroupByParameterFactory(
            view_type=ViewType.KANBAN.value)
        group_by_key_dtos = GroupBYKeyDTOFactory.create_batch(size=2)
        group_by_response_dtos = GroupByResponseDTOFactory.create_batch(size=2)
        return {
            "group_by_parameter": group_by_parameter,
            "group_by_key_dtos": group_by_key_dtos,
            "group_by_response_dtos": group_by_response_dtos
        }

    def test_given_valid_data_it_adds_group_by_for_list_and_returns_group_by_response_dto(
            self, interactor, storage, get_dtos_for_add_group_by_for_list,
            presenter
    ):
        group_by_key_dtos = \
            get_dtos_for_add_group_by_for_list["group_by_key_dtos"]
        group_by_parameter = \
            get_dtos_for_add_group_by_for_list["group_by_parameter"]
        add_or_edit_group_by_parameter_dto = \
            get_dtos_for_add_group_by_for_list[
                "add_or_edit_group_by_parameter_dto"
            ]
        group_by_response_dtos = \
            get_dtos_for_add_group_by_for_list["group_by_response_dtos"]
        storage.add_or_edit_group_by_for_list_view.return_value = \
            group_by_response_dtos[0]

        interactor.add_or_edit_group_by_wrapper(
            group_by_key_dtos=group_by_key_dtos,
            group_by_parameter=group_by_parameter,
            presenter=presenter
        )

        storage.add_or_edit_group_by_for_list_view.assert_called_once_with(
            add_or_edit_group_by_parameter_dto=
            add_or_edit_group_by_parameter_dto
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dtos=group_by_response_dtos
        )

    def test_given_empty_group_by_key_list_it_adds_group_by_for_list_and_returns_group_by_response_dto(
            self, interactor, storage, get_dtos_for_add_group_by_for_list,
            presenter
    ):
        group_by_key_dtos = []
        group_by_parameter = \
            get_dtos_for_add_group_by_for_list["group_by_parameter"]
        add_or_edit_group_by_parameter_dto = \
            get_dtos_for_add_group_by_for_list[
                "add_or_edit_group_by_parameter_dto"
            ]
        add_or_edit_group_by_parameter_dto.group_by_key = \
            GroupByKey.STAGE.value
        group_by_response_dtos = \
            get_dtos_for_add_group_by_for_list["group_by_response_dtos"]
        group_by_response_dtos[0].group_by_key = GroupByKey.STAGE.value
        storage.add_or_edit_group_by_for_list_view.return_value = \
            group_by_response_dtos[0]
        storage.get_group_by_dtos.return_value = None

        interactor.add_or_edit_group_by_wrapper(
            group_by_key_dtos=group_by_key_dtos,
            group_by_parameter=group_by_parameter,
            presenter=presenter
        )

        storage.add_or_edit_group_by_for_list_view.assert_called_once_with(
            add_or_edit_group_by_parameter_dto=
            add_or_edit_group_by_parameter_dto
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dtos=group_by_response_dtos
        )

    def test_given_valid_data_it_adds_group_by_for_kanban_and_returns_group_by_response_dto(
            self, interactor, storage, get_dtos_for_add_group_by_for_kanban,
            presenter
    ):
        group_by_key_dtos = \
            get_dtos_for_add_group_by_for_kanban["group_by_key_dtos"]
        group_by_parameter = \
            get_dtos_for_add_group_by_for_kanban["group_by_parameter"]
        group_by_response_dtos = \
            get_dtos_for_add_group_by_for_kanban["group_by_response_dtos"]
        storage.add_group_by_for_kanban_view_in_bulk.return_value = \
            group_by_response_dtos

        interactor.add_or_edit_group_by_wrapper(
            group_by_key_dtos=group_by_key_dtos,
            group_by_parameter=group_by_parameter,
            presenter=presenter
        )

        storage.add_group_by_for_kanban_view_in_bulk.assert_called_once_with(
            group_by_parameter=group_by_parameter,
            group_by_key_dtos=group_by_key_dtos
        )
        storage.delete_all_user_group_by.assert_called_once_with(
            user_id=group_by_parameter.user_id, view_type=group_by_parameter.view_type
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dtos=group_by_response_dtos
        )

    def test_given_empty_group_by_list_it_adds_group_by_for_kanban_and_returns_group_by_response_dto(
            self, interactor, storage, get_dtos_for_add_group_by_for_kanban,
            presenter
    ):
        group_by_key_dtos = []
        from ib_adhoc_tasks.interactors.dtos.dtos import GroupBYKeyDTO
        expected_group_by_key_dtos = [
            GroupBYKeyDTO(group_by_key='STAGE', order=1),
            GroupBYKeyDTO(group_by_key='ASSIGNEE', order=2)
        ]
        group_by_parameter = \
            get_dtos_for_add_group_by_for_kanban["group_by_parameter"]
        group_by_response_dtos = \
            get_dtos_for_add_group_by_for_kanban["group_by_response_dtos"]
        storage.add_group_by_for_kanban_view_in_bulk.return_value = \
            group_by_response_dtos
        storage.get_group_by_dtos.return_value = None

        interactor.add_or_edit_group_by_wrapper(
            group_by_key_dtos=group_by_key_dtos,
            group_by_parameter=group_by_parameter,
            presenter=presenter
        )

        storage.add_group_by_for_kanban_view_in_bulk.assert_called_once_with(
            group_by_parameter=group_by_parameter,
            group_by_key_dtos=expected_group_by_key_dtos
        )
        storage.delete_all_user_group_by.assert_called_once_with(
            user_id=group_by_parameter.user_id, view_type=group_by_parameter.view_type
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dtos=group_by_response_dtos
        )

    # todo need to write tests for exception cases
