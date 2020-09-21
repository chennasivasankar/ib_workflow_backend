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
        .get_group_by_presenter_interface import GetGroupByPresenterInterface
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
        group_by_response_dto = GroupByResponseDTOFactory()
        project_id = "project_id_1"
        user_id = "user_id_1"

        actual_group_by_response_dtos = interactor.get_group_by_wrapper(
            project_id=project_id, user_id=user_id, presenter=presenter
        )

