# from unittest.mock import create_autospec
#
# import pytest
#
# from ib_tasks.interactors.get_task_fields_and_actions_interactor import \
#     GetTaskFieldsAndActionsInteractor
# from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionDTO
# from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
# from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
# from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
#     TaskStorageInterface
#
# from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
#
# # TODO: Pending
# class TestGetFieldsAndActionsInteractor:
#
#     @pytest.fixture()
#     def get_task_dtos(self):
#         GetTaskDetailsDTOFactory.reset_sequence()
#         return  GetTaskDetailsDTOFactory.create_batch(size=10)
#
#
#     @pytest.fixture()
#     def expected_response(self):
#         response = GetTaskStageCompleteDetailsDTO(
#             fields_dto=[FieldDetailsDTO(
#                 field_type="Text field",
#                 key="requester",
#                 value="KC"
#             )],
#             actions_dto=[ActionDTO(
#
#             )]
#         )
#     def test_get_actions_given_valid_task_template_id_and_stage_id(self,
#                                                                    get_task_dtos):
#         # Arrange
#         storage = create_autospec(TaskStorageInterface)
#         interactor = GetTaskFieldsAndActionsInteractor(
#             storage=storage
#         )
#
#         # Act
#         response = interactor.get_task_fields_and_action(get_task_dtos)
#
#         # Assert
