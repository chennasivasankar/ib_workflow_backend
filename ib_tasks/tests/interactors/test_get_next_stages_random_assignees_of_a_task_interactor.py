import pytest
from mock import create_autospec

from ib_tasks.interactors.get_next_stages_random_assignees_of_a_task_interactor import \
    GetNextStagesRandomAssigneesOfATaskInteractor, InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.interactors.stages_dtos import StageWithUserDetailsDTO
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    prepare_permitted_user_details_mock

from ib_tasks.tests.factories.storage_dtos import StatusVariableDTOFactory, \
    StageRoleDTOFactory, StageDetailsDTOFactory


class TestGetNextStagesRandomAssigneesOfATaskInteractor:
    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        stage_storage = create_autospec(
            StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @staticmethod
    def stage_display_mock(mocker):
        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
               '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.get_next_stages_random_assignees_of_a_task_presenter import \
            GetNextStagesRandomAssigneesOfATaskPresenterInterface
        presenter_mock = create_autospec(
            GetNextStagesRandomAssigneesOfATaskPresenterInterface)
        return presenter_mock

    @staticmethod
    @pytest.fixture()
    def stage_display_value():
        from ib_tasks.tests.factories.storage_dtos \
            import StageDisplayValueDTOFactory
        StageDisplayValueDTOFactory.reset_sequence(0)
        stage_values = [
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory()
        ]
        return stage_values

    @staticmethod
    def test_given_invalid_path_raises_exception(storage_mock,
                                                 stage_storage_mock,
                                                 action_storage_mock,
                                                 task_storage_mock,
                                                 presenter_mock):
        # Arrange
        task_id = 1
        action_id = 1
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_id=task_id, presenter=presenter_mock)

        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)
        presenter_mock.raise_invalid_path_not_found_exception.assert_called_once_with(
            path_name)

    @staticmethod
    def test_given_invalid_method_name_raises_exception(mocker, storage_mock,
                                                        stage_storage_mock,
                                                        action_storage_mock,
                                                        task_storage_mock,
                                                        presenter_mock):
        # Arrange
        task_id = 1
        action_id = 1

        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(
            method_name="stage_1_action_name_1")
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        interactor \
                .get_next_stages_random_assignees_of_a_task_wrapper(
                action_id=action_id, task_id=task_id, presenter=presenter_mock
            )

        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)
        presenter_mock.raise_invalid_method_not_found_exception.assert_called_once_with(method_name="stage_1_action_name_1")

    @staticmethod
    def test_assert_called_with_expected_arguments(mocker, storage_mock,
                                                   stage_storage_mock,
                                                   action_storage_mock,
                                                   task_storage_mock,
                                                   presenter_mock):
        # Arrange
        mock_task_dict = {'status_variables': {'variable_1': 'stage_1'}}
        action_id = 1
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"
        mock_obj = mocker.patch(path_name)

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_id=task_id, presenter=presenter_mock
        )

        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={}
        )
        storage_mock.get_global_constants_to_task \
            .assert_called_once_with(task_id=task_id)
        storage_mock.get_stage_dtos_to_task \
            .assert_called_once_with(task_id=task_id)

    @staticmethod
    def test_access_invalid_key_raises_invalid_key_error(storage_mock,
                                                         presenter_mock,
                                                         stage_storage_mock,
                                                         action_storage_mock,
                                                         task_storage_mock):
        # Arrange
        action_id = 1
        task_id = 1

        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError

        # Act
        interactor \
                .get_next_stages_random_assignees_of_a_task_wrapper(
                action_id=action_id, task_id=task_id, presenter=presenter_mock
            )
        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        presenter_mock.raise_invalid_key_error.assert_called_once()

    @staticmethod
    def test_given_valid_details_updates_statuses(storage_mock,
                                                  stage_storage_mock,
                                                  action_storage_mock,
                                                  task_storage_mock):
        # Arrange
        action_id = 1
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_3"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        from ib_tasks.interactors.storage_interfaces.status_dtos import \
            StatusVariableDTO
        expected_status = [
            StatusVariableDTO(status_id=1, status_variable='variable_1',
                              value='stage_2')
        ]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        actual_result = interactor.get_status_variables_dtos_of_task_based_on_action(
            action_id=action_id, task_id=task_id)
        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
        assert expected_status == actual_result

    def test_given_valid_details_get_valid_next_stages_of_task(self,
                                                               mocker,
                                                               storage_mock,
                                                               stage_storage_mock,
                                                               action_storage_mock,
                                                               task_storage_mock,
                                                               stage_display_value):
        # Arrange
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_3"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = StatusVariableDTOFactory.create_batch(3)
        expected_status = statuses
        storage_mock.get_status_variables_to_task.return_value = statuses
        storage_mock.get_task_template_stage_logic_to_task \
            .return_value = stage_display_value
        storage_mock.validate_task_id.return_value = True
        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()
        status_stage_dtos = StatusOperandStageDTOFactory.create_batch(3)
        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        actual_result = interactor.get_next_stages_of_task(
            task_id=task_id, status_variable_dtos=statuses)
        # Assert

        assert actual_result == ['stage_1', 'stage_2', 'stage_3']

    def test_given_valid_details_get_permitted_users(self, mocker,
                                                     storage_mock,
                                                     stage_storage_mock,
                                                     action_storage_mock,
                                                     task_storage_mock,
                                                     presenter_mock,
                                                     stage_display_value):
        # Arrange
        action_id = 1
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_3"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        StageDetailsDTOFactory.reset_sequence()
        StageRoleDTOFactory.reset_sequence()
        statuses = StatusVariableDTOFactory.create_batch(3)
        stage_details_dto = StageDetailsDTOFactory.create_batch(3)
        stage_role_dtos = StageRoleDTOFactory.create_batch(3)
        storage_mock.get_status_variables_to_task.return_value = statuses
        storage_mock.get_task_template_stage_logic_to_task \
            .return_value = stage_display_value
        storage_mock.validate_task_id.return_value = True
        stage_with_user_details_dtos = [
            StageWithUserDetailsDTO(db_stage_id=1, stage_display_name='name_0',
                                    assignee_id='user_id_1',
                                    assignee_name='user_name_1',
                                    profile_pic_url='profile_pic_1'),
            StageWithUserDetailsDTO(db_stage_id=2, stage_display_name='name_1',
                                    assignee_id='user_id_1',
                                    assignee_name='user_name_1',
                                    profile_pic_url='profile_pic_1'),
            StageWithUserDetailsDTO(db_stage_id=3, stage_display_name='name_2',
                                    assignee_id='user_id_1',
                                    assignee_name='user_name_1',
                                    profile_pic_url='profile_pic_1')]
        from ib_tasks.tests.factories.interactor_dtos \
            import StatusOperandStageDTOFactory
        StatusOperandStageDTOFactory.reset_sequence()
        status_stage_dtos = StatusOperandStageDTOFactory.create_batch(3)
        mock_obj = self.stage_display_mock(mocker)
        mock_obj.return_value = status_stage_dtos
        stage_storage_mock. \
            get_stage_detail_dtos_given_stage_ids.return_value = \
            stage_details_dto
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value = \
            stage_role_dtos

        user_details_mock = prepare_permitted_user_details_mock(mocker)
        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock
        )

        # Act
        interactor.get_next_stages_random_assignees_of_a_task_wrapper(
            task_id=task_id, action_id=action_id, presenter=presenter_mock)
        # Assert
        presenter_mock. \
            get_next_stages_random_assignees_of_a_task_response.assert_called_once_with(
            stage_with_user_details_dtos)
