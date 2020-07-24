# from unittest import TestCase
# from unittest.mock import create_autospec
# from ib_tasks.interactors.user_action_on_task_interactor \
#     import UserActionOnTaskInteractor
# from ib_tasks.interactors.storage_interfaces.storage_interface \
#     import StorageInterface
# from ib_tasks.interactors.presenter_interfaces\
#     .user_action_on_task_presenter_interface \
#     import UserActionOnTaskPresenterInterface
#
#
# class TestUserActionOnTaskInteractor(TestCase):
#
#     @staticmethod
#     def test_given_invalid_board_id_raises_exception(mocker:
#         # Arrange
#         user_id = "user_1"
#         board_id = "board_1"
#         task_id = "task_1"
#         action_id = "action_1"
#         storage = create_autospec(StorageInterface)
#         from ib_tasks.tests.common_fixtures.adapters.boards_service \
#             import prepare_response_for_invalid_board
#         mocker_obj = prepare_response_for_invalid_board(mocker)
#         presenter = create_autospec(UserActionOnTaskPresenterInterface)
#         presenter
#         interactor = UserActionOnTaskInteractor(
#             user_id=user_id, board_id=board_id,
#             task_id=task_id, action_id=action_id,
#             storage=storage
#         )
#
#         # Act
#         response = interactor.user_action_on_task_wrapper(presenter=presenter)
#
#         # Assert
#         mocker_obj.assert_called_once()
#
