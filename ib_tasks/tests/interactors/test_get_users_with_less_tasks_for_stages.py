import pytest
from mock import create_autospec

from ib_tasks.tests.factories.interactor_dtos import \
    TaskWithDbStageIdDTOFactory, AssigneeCurrentTasksCountDTOFactory
from ib_tasks.tests.factories.storage_dtos import StageDetailsDTOFactory, \
    StageRoleDTOFactory


class TestGetUsersWithLessTasksInGivenStagesInteractor:
    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return create_autospec(ActionStorageInterface)

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import \
            StageStorageInterface
        return create_autospec(StageStorageInterface)

    @pytest.fixture
    def stage_details_dtos(self):
        StageDetailsDTOFactory.reset_sequence()
        return StageDetailsDTOFactory.create_batch(4)

    @pytest.fixture
    def stage_role_dtos(self):
        StageRoleDTOFactory.reset_sequence()
        return StageRoleDTOFactory.create_batch(4)

    def test_given_more_task_count_for_user_get_users_with_less_tasks_for_stages(
            self, mocker, stage_storage_mock, task_stage_storage_mock,
            action_storage_mock, stage_details_dtos, stage_role_dtos,
            snapshot):
        # Arrange
        TaskWithDbStageIdDTOFactory.reset_sequence()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.return_value \
            = stage_details_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value \
            = stage_role_dtos
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user. \
            return_value = [AssigneeCurrentTasksCountDTOFactory(
            assignee_id="user_id_2", tasks_count=2)]
        stage_storage_mock. \
            get_current_stages_of_all_tasks.return_value = \
            TaskWithDbStageIdDTOFactory.create_batch(2, task_id=1)
        action_storage_mock.get_stage_ids_having_actions.return_value = [1, 2]
        from ib_tasks.tests.common_fixtures.adapters.auth_service \
            import prepare_permitted_multiple_user_details_mock
        permitted_user_details_mock_method = \
            prepare_permitted_multiple_user_details_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_team_info_for_given_user_ids_mock
        get_team_info_for_given_user_ids_mock_method = \
            get_team_info_for_given_user_ids_mock(mocker)

        from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
            GetUsersWithLessTasksInGivenStagesInteractor
        get_users_with_less_tasks_interactor = \
            GetUsersWithLessTasksInGivenStagesInteractor(
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock,
                task_stage_storage=task_stage_storage_mock)
        # Act
        response = get_users_with_less_tasks_interactor.get_users_with_less_tasks_in_given_stages(
            stage_ids=["stage_id_3", "stage_id_4"], project_id="project_id_1")

        # Assert
        snapshot.assert_match(response)
        stage_storage_mock.get_current_stages_of_all_tasks.assert_called_once()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.assert_called_once()
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.assert_called_once()
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user.assert_called_once()
        stage_storage_mock. \
            get_current_stages_of_all_tasks.assert_called_once()
        action_storage_mock.get_stage_ids_having_actions.assert_called_once()

    def test_given_no_task_count_for_user_get_users_with_less_tasks_for_stages(
            self, mocker, stage_storage_mock, task_stage_storage_mock,
            action_storage_mock, stage_details_dtos, stage_role_dtos,
            snapshot):
        # Arrange
        TaskWithDbStageIdDTOFactory.reset_sequence()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.return_value \
            = stage_details_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value \
            = stage_role_dtos
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user. \
            return_value = []
        stage_storage_mock. \
            get_current_stages_of_all_tasks.return_value = \
            TaskWithDbStageIdDTOFactory.create_batch(2, task_id=1)
        action_storage_mock.get_stage_ids_having_actions.return_value = [1, 2]
        from ib_tasks.tests.common_fixtures.adapters.auth_service \
            import prepare_permitted_multiple_user_details_mock
        permitted_user_details_mock_method = \
            prepare_permitted_multiple_user_details_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_team_info_for_given_user_ids_mock
        get_team_info_for_given_user_ids_mock_method = \
            get_team_info_for_given_user_ids_mock(mocker)

        from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
            GetUsersWithLessTasksInGivenStagesInteractor
        get_users_with_less_tasks_interactor = \
            GetUsersWithLessTasksInGivenStagesInteractor(
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock,
                task_stage_storage=task_stage_storage_mock)
        # Act
        response = get_users_with_less_tasks_interactor. \
            get_users_with_less_tasks_in_given_stages(
            stage_ids=["stage_id_2", "stage_id_3", "stage_id_4"],
            project_id="project_id_1")

        # Assert
        snapshot.assert_match(response)
        stage_storage_mock.get_current_stages_of_all_tasks.assert_called_once()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.assert_called_once()
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.assert_called_once()
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user.assert_called_once()
        stage_storage_mock. \
            get_current_stages_of_all_tasks.assert_called_once()
        action_storage_mock.get_stage_ids_having_actions.assert_called_once()


    def test_given_equal_task_count_for_user_get_users_with_less_tasks_for_stages(
            self, mocker, stage_storage_mock, task_stage_storage_mock,
            action_storage_mock, stage_details_dtos, stage_role_dtos,
            snapshot):
        # Arrange
        TaskWithDbStageIdDTOFactory.reset_sequence()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.return_value \
            = stage_details_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value \
            = stage_role_dtos
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user. \
            return_value = [AssigneeCurrentTasksCountDTOFactory(
            assignee_id="user_id_1", tasks_count=1), AssigneeCurrentTasksCountDTOFactory(
            assignee_id="user_id_0", tasks_count=1)]
        stage_storage_mock. \
            get_current_stages_of_all_tasks.return_value = \
            TaskWithDbStageIdDTOFactory.create_batch(2, task_id=1)
        action_storage_mock.get_stage_ids_having_actions.return_value = [1, 2]
        from ib_tasks.tests.common_fixtures.adapters.auth_service \
            import prepare_permitted_multiple_user_details_mock
        permitted_user_details_mock_method = \
            prepare_permitted_multiple_user_details_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_team_info_for_given_user_ids_mock
        get_team_info_for_given_user_ids_mock_method = \
            get_team_info_for_given_user_ids_mock(mocker)

        from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
            GetUsersWithLessTasksInGivenStagesInteractor
        get_users_with_less_tasks_interactor = \
            GetUsersWithLessTasksInGivenStagesInteractor(
                action_storage=action_storage_mock,
                stage_storage=stage_storage_mock,
                task_stage_storage=task_stage_storage_mock)
        # Act
        response = get_users_with_less_tasks_interactor.get_users_with_less_tasks_in_given_stages(
            stage_ids=["stage_id_3", "stage_id_4"], project_id="project_id_1")

        # Assert
        snapshot.assert_match(response)
        stage_storage_mock.get_current_stages_of_all_tasks.assert_called_once()
        stage_storage_mock.get_stage_detail_dtos_given_stage_ids.assert_called_once()
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.assert_called_once()
        task_stage_storage_mock.get_count_of_tasks_assigned_for_each_user.assert_called_once()
        stage_storage_mock. \
            get_current_stages_of_all_tasks.assert_called_once()
        action_storage_mock.get_stage_ids_having_actions.assert_called_once()

