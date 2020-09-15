import pytest

from ib_boards.adapters.iam_service import InvalidProjectIdsException
from ib_boards.exceptions.custom_exceptions import InvalidBoardIdsException
from ib_boards.interactors.storage_interfaces.storage_interface import StorageInterface


class TestAddProjectForBoards:

    @pytest.fixture
    def project_board_dtos(self):
        from ib_boards.tests.factories.interactor_dtos import \
            ProjectBoardDTOFactory
        ProjectBoardDTOFactory.reset_sequence()
        dtos = ProjectBoardDTOFactory.create_batch(size=3)
        return dtos

    @pytest.fixture
    def storage_mock(self):
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    def test_given_invalid_board_ids_raise_exception(self,
                                                     mocker,
                                                     project_board_dtos,
                                                     storage_mock):
        # Arrange
        valid_board_ids = ["BOARD_ID_0", "BOARD_ID_1"]
        board_ids = ["BOARD_ID_0", "BOARD_ID_1", "BOARD_ID_2"]
        project_ids = ["PROJECT_ID_0", "PROJECT_ID_1", "PROJECT_ID_2"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.interactors.add_project_for_boards import \
            AddProjectForBoardsInteractor
        interactor = AddProjectForBoardsInteractor(storage=storage_mock)
        storage_mock.get_valid_board_ids.return_value = valid_board_ids

        # Act
        with pytest.raises(InvalidBoardIdsException) as err:
            interactor.add_project_for_boards(project_board_dtos)

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(board_ids)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )

    def test_given_invalid_project_ids_raise_exception(self,
                                                       mocker,
                                                       project_board_dtos,
                                                       storage_mock):
        # Arrange
        project_ids = ["PROJECT_ID_0", "PROJECT_ID_1", "PROJECT_ID_2"]
        valid_project_ids = ["PROJECT_ID_1", "PROJECT_ID_2"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker,
                                                         valid_project_ids)
        from ib_boards.interactors.add_project_for_boards import \
            AddProjectForBoardsInteractor
        interactor = AddProjectForBoardsInteractor(storage=storage_mock)

        # Act
        with pytest.raises(InvalidProjectIdsException) as err:
            interactor.add_project_for_boards(project_board_dtos)

        # Assert
        project_adapter_mock.assert_called_once_with(
            project_ids
        )

    def test_given_valid_details_updates_project_id_for_boards(
            self, mocker, project_board_dtos, storage_mock):
        # Arrange
        board_ids = ["BOARD_ID_0", "BOARD_ID_1", "BOARD_ID_2"]
        project_ids = ["PROJECT_ID_0", "PROJECT_ID_1", "PROJECT_ID_2"]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)
        from ib_boards.interactors.add_project_for_boards import \
            AddProjectForBoardsInteractor
        interactor = AddProjectForBoardsInteractor(storage=storage_mock)
        storage_mock.get_valid_board_ids.return_value = board_ids

        # Act
        interactor.add_project_for_boards(project_board_dtos)

        # Assert
        storage_mock.get_valid_board_ids.assert_called_once_with(board_ids)
        project_adapter_mock.assert_called_once_with(
            project_ids
        )
        storage_mock.add_project_id_for_boards.assert_called_once_with(
            project_board_dtos
        )
