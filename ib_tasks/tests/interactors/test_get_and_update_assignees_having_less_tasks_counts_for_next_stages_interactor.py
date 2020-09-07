from unittest.mock import create_autospec, patch

import factory
import pytest
from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
    GetUsersWithLessTasksInGivenStagesInteractor
from ib_tasks.interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory, \
    UserIdWIthTeamDetailsDTOFactory, TeamDetailsDTOFactory
from ib_tasks.tests.factories.interactor_dtos import \
    StageWithUserDetailsDTOFactory, StageAssigneeDTOFactory


class TestGetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor:
    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.\
            action_storage_interface import ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.\
            stages_storage_interface import StageStorageInterface
        stage_storage = create_autospec(
            StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
            TaskStageStorageInterface
        task_stage_storage = create_autospec(
            TaskStageStorageInterface)
        return task_stage_storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageWithUserDetailsDTOFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()
        UserIdWIthTeamDetailsDTOFactory.reset_sequence()
        TeamDetailsDTOFactory.reset_sequence()
        StageAssigneeDTOFactory.reset_sequence()

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(GetUsersWithLessTasksInGivenStagesInteractor,
                  'get_users_with_less_tasks_in_given_stages')
    def test_given_valid_details_get_next_stage_assignees_and_update_in_db(
            self,
            users_with_less_tasks_mock, update_task_stage_assignees_mock,
            storage_mock,
            stage_storage_mock, action_storage_mock,
            task_storage_mock, task_stage_storage_mock):
        # Arrange
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_storage_mock.get_project_id_of_task.return_value = "project_1"
        stage_storage_mock. \
            get_virtual_stages_already_having_in_task.return_value = []

        stage_storage_mock. \
            get_stage_ids_excluding_virtual_stages.return_value = \
            ['stage_1', 'stage_2', 'stage_3']
        given_stage_ids = [2, 3]
        from ib_tasks.interactors.stages_dtos import \
            StageWithUserDetailsAndTeamDetailsDTO
        stage_with_user_details_and_team_details_dto = \
            StageWithUserDetailsAndTeamDetailsDTO(
                stages_with_user_details_dtos=
                StageWithUserDetailsDTOFactory.create_batch(
                    2, db_stage_id=factory.Iterator(given_stage_ids)),
                user_with_team_details_dtos=[
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174000",
                        team_details=TeamDetailsDTOFactory(team_id='team_1')),
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174001",
                        team_details=TeamDetailsDTOFactory(team_id='team_2'))])
        users_with_less_tasks_mock.return_value = \
            stage_with_user_details_and_team_details_dto

        from ib_tasks.interactors. \
            get_and_update_assignees_having_less_tasks_counts_for_next_stages_interactor import \
            GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor
        interactor = GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_random_assignees_of_next_stages_and_update_in_db(
            stage_ids=['stage_2', 'stage_3'], task_id=1)

        # Assert
        from ib_tasks.interactors.stages_dtos import \
            TaskIdWithStageAssigneesDTO
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=1, stage_assignees=StageAssigneeDTOFactory.create_batch(
                2, db_stage_id=factory.Iterator(given_stage_ids),
                assignee_id=factory.Iterator(
                    ["123e4567-e89b-12d3-a456-426614174000",
                     "123e4567-e89b-12d3-a456-426614174001"])))
        update_task_stage_assignees_mock.assert_called_once_with(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(GetUsersWithLessTasksInGivenStagesInteractor,
                  'get_users_with_less_tasks_in_given_stages')
    def test_given_valid_details_with_virtual_stages_get_next_stage_assignees_and_update_in_db(
            self,
            users_with_less_tasks_mock, update_task_stage_assignees_mock,
            storage_mock,
            stage_storage_mock, action_storage_mock,
            task_storage_mock, task_stage_storage_mock):
        # Arrange
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_storage_mock.get_project_id_of_task.return_value = "project_1"
        stage_storage_mock. \
            get_virtual_stages_already_having_in_task.return_value = []

        stage_storage_mock. \
            get_stage_ids_excluding_virtual_stages.return_value = \
            ['stage_1', 'stage_2', 'stage_3']
        stage_storage_mock. \
            get_db_stage_ids_for_given_stage_ids.return_value = [4, 5]
        given_stage_ids = [2, 3, 4, 5]
        from ib_tasks.interactors.stages_dtos import \
            StageWithUserDetailsAndTeamDetailsDTO
        stage_with_user_details_and_team_details_dto = \
            StageWithUserDetailsAndTeamDetailsDTO(
                stages_with_user_details_dtos=
                StageWithUserDetailsDTOFactory.create_batch(
                    2, db_stage_id=factory.Iterator(given_stage_ids)),
                user_with_team_details_dtos=[
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174000",
                        team_details=TeamDetailsDTOFactory(team_id='team_1')),
                    UserIdWIthTeamDetailsDTOFactory(
                        user_id="123e4567-e89b-12d3-a456-426614174001",
                        team_details=TeamDetailsDTOFactory(team_id='team_2'))])
        users_with_less_tasks_mock.return_value = \
            stage_with_user_details_and_team_details_dto

        from ib_tasks.interactors. \
            get_and_update_assignees_having_less_tasks_counts_for_next_stages_interactor import \
            GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor
        interactor = GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_random_assignees_of_next_stages_and_update_in_db(
            stage_ids=['stage_2', 'stage_3'], task_id=1)

        # Assert
        from ib_tasks.interactors.stages_dtos import \
            TaskIdWithStageAssigneesDTO
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=1, stage_assignees=StageAssigneeDTOFactory.create_batch(
                2, db_stage_id=factory.Iterator(given_stage_ids),
                assignee_id=factory.Iterator(
                    ["123e4567-e89b-12d3-a456-426614174000",
                     "123e4567-e89b-12d3-a456-426614174001"])))

        task_stage_storage_mock.\
            create_task_stage_history_records_for_virtual_stages.\
            assert_called_once_with(stage_ids=[4, 5], task_id=1)
        update_task_stage_assignees_mock.assert_called_once_with(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)
