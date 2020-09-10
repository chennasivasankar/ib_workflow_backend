import pytest
from mock import create_autospec


class TestGetStagesAssigneesDetailsInteractor:

    @pytest.fixture
    def task_stage_storage(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface \
            import \
            TaskStageStorageInterface
        task_stage_storage = create_autospec(TaskStageStorageInterface)
        return task_stage_storage

    @pytest.fixture
    def interactor(self, task_stage_storage):
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import \
            GetStagesAssigneesDetailsInteractor
        interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=task_stage_storage
        )
        return interactor

    @pytest.fixture
    def reset_sequence(self):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskStageAssigneeDTOFactory
        TaskStageAssigneeDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            AssigneeWithTeamDetailsDTOFactory
        AssigneeWithTeamDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.adapter_dtos import TeamInfoDTOFactory
        TeamInfoDTOFactory.reset_sequence()

    @pytest.fixture
    def stage_assignee_dtos(self, reset_sequence):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskStageAssigneeDTOFactory
        stage_assignee_dtos = [
            TaskStageAssigneeDTOFactory(),
            TaskStageAssigneeDTOFactory(),
            TaskStageAssigneeDTOFactory(),
            TaskStageAssigneeDTOFactory(assignee_id=None, team_id=None)
        ]
        return stage_assignee_dtos

    @pytest.fixture
    def stage_assignee_details_dtos(
            self, reset_sequence
    ):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeWithTeamDetailsDTOFactory
        stage_assignee_details_dtos = \
            StageAssigneeWithTeamDetailsDTOFactory.create_batch(
                size=3,
            )
        stage_assignee_details_dto = [StageAssigneeWithTeamDetailsDTOFactory(
            assignee_details_dto=None
        )]
        stage_assignee_details_dtos = stage_assignee_details_dtos + \
                                    stage_assignee_details_dto
        return stage_assignee_details_dtos

    def test_given_task_id_and_stage_ids_invalid_stages_for_task_raise_exception(
            self, interactor, task_stage_storage, reset_sequence
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStageIdsForTask
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS_FOR_TASK
        task_id = 1
        stage_ids = [3, 5, 7, 8]
        valid_stage_ids = [3, 5]
        invalid_stage_ids = [7, 8]
        project_id = "FIN MAN"
        exception_message = INVALID_STAGE_IDS_FOR_TASK.format(
            invalid_stage_ids, task_id
        )
        task_stage_storage.get_valid_stage_ids_of_task.return_value = \
            valid_stage_ids

        # Act
        with pytest.raises(InvalidStageIdsForTask) as err:
            interactor.get_stages_assignee_details_dtos(
                task_id=task_id, stage_ids=stage_ids, project_id=project_id
            )
        exception_objects = err.value
        # Assert
        task_stage_storage.get_valid_stage_ids_of_task.assert_called_once_with(
            task_id, stage_ids)
        assert exception_objects.message == exception_message

    def test_given_task_id_and_stage_ids_returns_stage_assignee_dtos(
            self, task_stage_storage, interactor, stage_assignee_dtos,
            mocker, reset_sequence, stage_assignee_details_dtos
    ):
        # Arrange
        task_id = 1
        stage_ids = [
            stage_assignee_dto.stage_id
            for stage_assignee_dto in stage_assignee_dtos
        ]
        project_id = "FIN MAN"
        from ib_tasks.tests.common_fixtures.adapters \
            .assignees_details_service import \
            assignee_details_dtos_mock
        assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_id_team_details_dtos_mock

        get_user_id_team_details_dtos_mock_method = \
            get_user_id_team_details_dtos_mock(
                mocker)
        valid_stage_ids = stage_ids
        task_stage_storage.get_valid_stage_ids_of_task.return_value = \
            valid_stage_ids
        task_stage_storage.get_stage_assignee_dtos.return_value = \
            stage_assignee_dtos

        # Act
        response = interactor.get_stages_assignee_details_dtos(
            task_id=task_id, stage_ids=stage_ids, project_id=project_id
        )

        # Assert
        assert response == stage_assignee_details_dtos
        task_stage_storage.get_stage_assignee_dtos.assert_called_once_with(
            task_id, stage_ids)
        assignee_details_dtos_mock_method.assert_called_once()
        get_user_id_team_details_dtos_mock_method.assert_called_once()
