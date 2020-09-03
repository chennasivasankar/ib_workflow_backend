from unittest.mock import Mock

import pytest
from mock import create_autospec

from ib_tasks.interactors.filter_dtos import SearchQueryWithPaginationDTO


class TestGetStageSearchablePossibleAssigneesInteractor:

    @pytest.fixture
    def stage_storage(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        stage_storage = create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def interactor(self, stage_storage, task_storage):
        from ib_tasks.interactors. \
            get_stage_searchable_possible_assignees_interactor \
            import GetStageSearchablePossibleAssigneesInteractor
        interactor = GetStageSearchablePossibleAssigneesInteractor(
            stage_storage=stage_storage, task_storage=task_storage
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
            self, interactor, stage_storage, task_storage,
            presenter_mock, limit
    ):
        # Arrange
        stage_id = 1
        task_id = "IBWF-1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=limit, offset=0, search_query='iB'
        )

        # Act
        interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
                stage_id=stage_id, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto,
                presenter=presenter_mock
            )

        # Assert
        presenter_mock.raise_invalid_limit_exception.assert_called_once()

    @pytest.mark.parametrize('offset', [-1, -5])
    def test_with_invalid_offset_raises_exception(
            self, interactor, stage_storage, task_storage,
            presenter_mock, offset
    ):
        # Arrange
        stage_id = 1
        task_id = "IBWF-1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=offset, search_query='iB'
        )

        # Act
        interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
                stage_id=stage_id, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto,
                presenter=presenter_mock
            )

        # Assert
        presenter_mock.raise_invalid_offset_exception.assert_called_once()

    def test_with_invalid_stage_id_raises_exception(
            self, interactor, stage_storage, task_storage,
            presenter_mock, mocker
    ):
        # Arrange
        stage_id = 1
        task_id = "IBWF-1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=0, search_query='iB'
        )
        task_storage.check_is_valid_task_display_id.return_value = True
        stage_storage.check_is_stage_exists.return_value = False
        mock_obj = Mock()
        presenter_mock.raise_invalid_stage_id_exception.return_value = mock_obj

        # Act
        result = interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
                stage_id=stage_id, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto,
                presenter=presenter_mock
            )

        # Assert
        assert result == mock_obj
        stage_storage.check_is_stage_exists.assert_called_once_with(
            stage_id=stage_id)
        presenter_mock.raise_invalid_stage_id_exception.assert_called_once()

    def test_with_invalid_task_display_id_raises_exception(
            self, interactor, stage_storage, task_storage,
            presenter_mock
    ):
        # Arrange
        stage_id = 1
        task_id = "IBWF-1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=0, search_query='iB'
        )
        task_storage.check_is_valid_task_display_id.return_value = False
        mock_obj = Mock()
        presenter_mock.raise_invalid_task_display_id_exception.return_value = \
            mock_obj

        # Act
        result = interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
                stage_id=stage_id, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto,
                presenter=presenter_mock
            )

        # Assert
        assert result == mock_obj
        task_storage.check_is_valid_task_display_id.assert_called_once()
        presenter_mock.raise_invalid_task_display_id_exception. \
            assert_called_once()

    def test_with_valid_details_returns_assignee_details(
            self, interactor, stage_storage, task_storage,
            presenter_mock, mocker
    ):
        # Arrange
        stage_id = 1
        task_id = "IBWF-1"
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            limit=1, offset=0, search_query='iB'
        )

        from ib_tasks.tests.factories.adapter_dtos import \
            UserIdWIthTeamDetailsDTOFactory, TeamDetailsDTOFactory, \
            UserDetailsDTOFactory
        UserIdWIthTeamDetailsDTOFactory.reset_sequence()
        TeamDetailsDTOFactory.reset_sequence()
        UserDetailsDTOFactory.reset_sequence()

        user_details_dtos = UserDetailsDTOFactory.create_batch(size=2)
        user_id_with_team_details_dtos = \
            UserIdWIthTeamDetailsDTOFactory.create_batch(size=2)

        from ib_tasks.interactors.stages_dtos import \
            UserDetailsWithTeamDetailsDTO
        expected_output = UserDetailsWithTeamDetailsDTO(
            user_details_dtos=user_details_dtos,
            user_id_with_team_details_dtos=user_id_with_team_details_dtos)

        task_storage.check_is_valid_task_display_id.return_value = True
        stage_storage.check_is_stage_exists.return_value = True

        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_details_for_the_given_role_ids_based_on_query_mock, \
            get_team_info_for_given_user_ids_mock
        get_user_details_for_the_given_role_ids_based_on_query_mock(mocker)
        get_team_info_for_given_user_ids_mock(mocker)

        mock_obj = Mock()
        presenter_mock.get_stage_assignee_details_response.return_value = \
            mock_obj

        # Act
        result = interactor. \
            get_stage_searchable_possible_assignees_of_a_task_wrapper(
                stage_id=stage_id, task_id=task_id,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto,
                presenter=presenter_mock
            )

        # Assert
        assert result == mock_obj
        task_storage.check_is_valid_task_display_id.assert_called_once()
        stage_storage.check_is_stage_exists.assert_called_once_with(
            stage_id=stage_id)
        presenter_mock.get_stage_assignee_details_response. \
            assert_called_once_with(
                user_details_with_team_details_dto=expected_output
            )
