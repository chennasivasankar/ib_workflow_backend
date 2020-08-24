import pytest

from ib_boards.models import Board


@pytest.mark.django_db
class TestAddProjectIdForBoards:

    @pytest.fixture
    def project_board_dtos(self):
        from ib_boards.tests.factories.interactor_dtos import \
            ProjectBoardDTOFactory
        ProjectBoardDTOFactory.reset_sequence(1)
        dtos = ProjectBoardDTOFactory.create_batch(size=3)
        return dtos

    @pytest.fixture
    def populate_data(self):
        from ib_boards.tests.factories.models import BoardFactory
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=5, project_id=None)

    @staticmethod
    def _check_if_given_project_for_boards_created_correctly(expected, returned):
        for board_dto, board_obj in zip(expected, returned):
            assert board_dto.board_id == board_obj.board_id
            assert board_dto.project_id == board_obj.project_id

    def test_add_project_id_for_boards(self, project_board_dtos,
                                       populate_data):
        # Arrange
        board_ids = ["BOARD_ID_1", "BOARD_ID_2", "BOARD_ID_3"]
        from ib_boards.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        storage.add_project_id_for_boards(project_board_dtos)

        # Assert
        boards = Board.objects.filter(board_id__in=board_ids)
        self._check_if_given_project_for_boards_created_correctly(
            project_board_dtos, boards)
