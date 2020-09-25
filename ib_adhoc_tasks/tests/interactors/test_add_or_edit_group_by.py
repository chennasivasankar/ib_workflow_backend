import mock
import pytest


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

    def test_given_valid_data_it_adds_and_returns_group_by_dto(
            self, interactor, storage, presenter
    ):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory, AddOrEditGroupByParameterDTOFactory
        user_id = "user_id_1"
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
            group_by_id=None, user_id=user_id
        )
        group_by_response_dto = GroupByResponseDTOFactory()
        storage.add_group_by.return_value = group_by_response_dto
        storage.get_view_types_of_user.return_value = []
        presenter.get_response_for_add_or_edit_group_by.return_value = mock.Mock()

        interactor.add_or_edit_group_by_wrapper(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto,
            presenter=presenter
        )

        storage.get_view_types_of_user.assert_called_once_with(user_id=user_id)
        storage.add_group_by.assert_called_once_with(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dto=group_by_response_dto
        )

    def test_given_valid_data_it_edits_and_returns_group_by_dto(
            self, interactor, storage, presenter
    ):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory, AddOrEditGroupByParameterDTOFactory
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
            group_by_id=1
        )
        group_by_response_dto = GroupByResponseDTOFactory()
        storage.edit_group_by.return_value = group_by_response_dto
        presenter.get_response_for_add_or_edit_group_by.return_value = mock.Mock()

        interactor.add_or_edit_group_by_wrapper(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto,
            presenter=presenter
        )

        storage.edit_group_by.assert_called_once_with(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )
        presenter.get_response_for_add_or_edit_group_by.assert_called_once_with(
            group_by_response_dto=group_by_response_dto
        )
