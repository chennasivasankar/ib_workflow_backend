"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
import json

from ib_boards.interactors.dtos import StarredAndOtherBoardsDTO
from ib_boards.presenters.presenter_implementation import \
    GetBoardsPresenterImplementation


class TestGetBoardsPresenterImplementation:

    def test_get_response_for_user_have_no_access_for_boards(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_BOARDS
        expected_response = USER_NOT_HAVE_ACCESS_TO_BOARDS[0]
        expected_http_status_code = 403
        expected_res_status = USER_NOT_HAVE_ACCESS_TO_BOARDS[1]
        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_user_have_no_access_for_boards()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_invalid_offset(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            INVALID_OFFSET_VALUE
        expected_response = INVALID_OFFSET_VALUE[0]
        expected_http_status_code = 400
        expected_res_status = INVALID_OFFSET_VALUE[1]
        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_invalid_offset()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_invalid_limit(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            INVALID_LIMIT_VALUE
        expected_response = INVALID_LIMIT_VALUE[0]
        expected_http_status_code = 400
        expected_res_status = INVALID_LIMIT_VALUE[1]
        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_invalid_limit()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_get_boards(self, snapshot):
        # Arrange
        total_boards = 6
        from ib_boards.tests.factories.storage_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(3)
        starred_boards_dtos = BoardDTOFactory.create_batch(3)
        starred_and_other_boards_dto = StarredAndOtherBoardsDTO(
            starred_boards_dtos=starred_boards_dtos,
            other_boards_dtos=board_dtos
        )

        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_get_boards(
            starred_and_other_boards_dto=starred_and_other_boards_dto,
            total_boards=total_boards
        )

        # Assert
        actual_response_content = json.loads(actual_response.content)

        snapshot.assert_match(actual_response_content, 'boards')

    def test_get_response_for_get_boards_when_no_starred_boards(self, snapshot):
        # Arrange
        total_boards = 3
        from ib_boards.tests.factories.storage_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence()
        board_dtos = BoardDTOFactory.create_batch(3)
        starred_and_other_boards_dto = StarredAndOtherBoardsDTO(
            starred_boards_dtos=[],
            other_boards_dtos=board_dtos
        )

        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_get_boards(
            starred_and_other_boards_dto=starred_and_other_boards_dto,
            total_boards=total_boards
        )

        # Assert
        actual_response_content = json.loads(actual_response.content)

        snapshot.assert_match(actual_response_content, 'boards')

    def test_get_response_for_invalid_project_id(self):
        # Arrange
        from ib_boards.adapters.iam_service import InvalidProjectIdsException
        error = InvalidProjectIdsException(['project_id_1'])
        from ib_boards.constants.exception_messages import \
            INVALID_PROJECT_ID
        expected_response = INVALID_PROJECT_ID[0].format(error.invalid_project_ids[0])
        expected_http_status_code = 404
        expected_res_status = INVALID_PROJECT_ID[1]
        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_invalid_project_id(error)

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_user_is_not_in_project(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            USER_IS_NOT_IN_PROJECT
        expected_response = USER_IS_NOT_IN_PROJECT[0]
        expected_http_status_code = 403
        expected_res_status = USER_IS_NOT_IN_PROJECT[1]
        presenter = GetBoardsPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_user_is_not_in_project()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

