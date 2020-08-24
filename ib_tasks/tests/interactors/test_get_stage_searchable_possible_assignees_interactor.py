import pytest
from mock import create_autospec

from ib_tasks.interactors.get_stage_searchable_possible_assignees_interactor \
    import SearchQueryWithPaginationDTO


class TestGetStageSearchablePossibleAssigneesInteractor:

    @pytest.fixture
    def stage_storage(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        stage_storage = create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def interactor(self, stage_storage):
        from ib_tasks.interactors. \
            get_stage_searchable_possible_assignees_interactor \
            import GetStageSearchablePossibleAssigneesInteractor
        interactor = GetStageSearchablePossibleAssigneesInteractor(
            stage_storage=stage_storage
        )
        return interactor

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            get_stage_searchable_possible_assignees_presenter_interface \
            import GetStageSearchablePossibleAssigneesPresenterInterface
        presenter_mock = create_autospec(
            GetStageSearchablePossibleAssigneesPresenterInterface
        )
        return presenter_mock

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import SearchDTOFactory
        SearchDTOFactory.reset_sequence()

    @pytest.mark.parametrize('limit', [-1, 0, -5])
    def test_with_invalid_limit_raises_exception(
            self, interactor, stage_storage, presenter_mock, limit
    ):
        # Arrange
        stage_id = 1
        project_id = "project_1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=limit, offset=0, search_query='iB'
        )

        # Act
        interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
            stage_id=stage_id,
            search_query_with_pagination_dto=
            search_query_with_pagination_dto,
            presenter=presenter_mock, project_id=project_id
        )

        # Assert
        presenter_mock.raise_invalid_limit_exception.assert_called_once()

    @pytest.mark.parametrize('offset', [-1, -5])
    def test_with_invalid_offset_raises_exception(
            self, interactor, stage_storage, presenter_mock, offset
    ):
        # Arrange
        stage_id = 1
        project_id = "project_1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=offset, search_query='iB'
        )

        # Act
        interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
            stage_id=stage_id,
            search_query_with_pagination_dto=
            search_query_with_pagination_dto,
            presenter=presenter_mock, project_id=project_id
        )

        # Assert
        presenter_mock.raise_invalid_offset_exception.assert_called_once()

    def test_with_invalid_stage_id_raises_exception(
            self, interactor, stage_storage, presenter_mock, mocker
    ):
        # Arrange
        stage_id = 1
        project_id = "project_1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=0, search_query='iB'
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_details_for_the_given_role_ids_based_on_query
        mock_method = \
            get_user_details_for_the_given_role_ids_based_on_query(mocker)
        stage_storage.check_is_stage_exists.return_value = True
        presenter_mock.get_stage_assignee_details_response.return_value = \
            mock_method.return_value

        # Act
        result = interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
            stage_id=stage_id, project_id=project_id,
            search_query_with_pagination_dto=
            search_query_with_pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        assert result == mock_method.return_value
        stage_storage.check_is_stage_exists.assert_called_once_with(
            stage_id=stage_id)
        mock_method.assert_called_once()
        presenter_mock.get_stage_assignee_details_response. \
            assert_called_once_with(user_details_dtos=mock_method.return_value)
