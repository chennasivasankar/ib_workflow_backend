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
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .group_by_presenter_interface import \
            GetGroupByPresenterInterface
        return mock.create_autospec(GetGroupByPresenterInterface)

    @pytest.fixture
    def interactor(self, storage):
        from ib_adhoc_tasks.interactors.group_by_interactor import \
            GroupByInteractor
        return GroupByInteractor(storage=storage)

    def test_given_valid_data_it_returns_group_by_dtos(
            self, interactor, storage, presenter
    ):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        group_by_response_dtos = \
            GroupByResponseDTOFactory.create_batch(size=2)
        project_id = "project_id_1"
        user_id = "user_id_1"
        storage.get_group_by_dtos.return_value = group_by_response_dtos
        presenter.get_response_for_get_group_by.return_value = mock.Mock()

        interactor.get_group_by_wrapper(
            project_id=project_id, user_id=user_id, presenter=presenter
        )

        storage.get_group_by_dtos.assert_called_once_with(user_id=user_id)
        presenter.get_response_for_get_group_by.assert_called_once_with(
            group_by_response_dtos=group_by_response_dtos
        )
