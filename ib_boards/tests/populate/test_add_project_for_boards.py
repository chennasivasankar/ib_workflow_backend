import pytest

from ib_boards.models import Board
from ib_boards.populate.populate_script_for_add_project_for_boards import \
    populate_project_for_boards
from ib_boards.tests.factories.models import BoardFactory


@pytest.mark.django_db
class TestPopulateProjectForBoards:

    @pytest.fixture
    def populate_data(self):
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=4, project_id=None)

    @staticmethod
    def _check_if_given_project_for_boards_created_correctly(expected, returned):
        for board_dto, board_obj in zip(expected, returned):
            assert board_dto['board_id'] == board_obj.board_id
            assert board_dto['project_id'] == board_obj.project_id

    @pytest.fixture()
    def valid_format(self):
        valid_format = {
            "project_id": "project_id_2",
            "board_id": "board_id_2"
        }

        import json
        json_valid_format = json.dumps(valid_format)
        return json_valid_format

    def test_given_invalid_keys_raise_exception(self, valid_format):
        # Arrange
        valid_json_format = valid_format
        list_of_project_boards_dict = [
            {
                "invalid_field_name": "project_id_1",
                "board_id": "BOARD_ID_1"
            },
            {
                "project_id": "project_id_2",
                "board_id": "BOARD_ID_2"
            }
        ]

        # Act

        from ib_boards.exceptions.custom_exceptions import \
            InvalidFormatException
        with pytest.raises(InvalidFormatException) as err:
            populate_project_for_boards(list_of_project_boards_dict)

        # Assert
        assert err.value.valid_format == valid_json_format

    def test_given_valid_details_adds_project_id_for_boards(self,
                                                            mocker,
                                                            populate_data):
        # Arrange
        project_ids = ["project_id_1", "project_id_2"]
        list_of_project_boards_dict = [
            {
                "project_id": "project_id_1",
                "board_id": "BOARD_ID_1"
            },
            {
                "project_id": "project_id_2",
                "board_id": "BOARD_ID_2"
            }
        ]
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            mock_validate_project_ids
        project_adapter_mock = mock_validate_project_ids(mocker, project_ids)

        # Act
        populate_project_for_boards(list_of_project_boards_dict)

        # Assert
        board_ids = ["BOARD_ID_1", "BOARD_ID_2"]
        boards = Board.objects.filter(board_id__in=board_ids)
        self._check_if_given_project_for_boards_created_correctly(list_of_project_boards_dict,
                                                                  boards)
