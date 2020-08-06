import pytest
from mock import create_autospec

from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface


class TestGetStagesAssigneesDetailsInteractor:

    @pytest.fixture
    def interactor(self):
        task_stage_storage = create_autospec(TaskStageStorageInterface)
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import \
            GetStagesAssigneesDetailsInteractor
        interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=task_stage_storage
        )
        return interactor

    def test_given_task_id_and_stage_ids_invalid_stages_for_task_raise_exception(
            self, interactor
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStageIdsForTask
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS_FOR_TASK
        task_id = 1
        stage_ids = []
        invalid_stage_ids = []
        exception_message = INVALID_STAGE_IDS_FOR_TASK.format(
            invalid_stage_ids, task_id
        )

        # Act
        with pytest.raises(InvalidStageIdsForTask) as err:
            interactor.get_stages_assignee_details_dtos(
                task_id=task_id, stage_ids=stage_ids
            )

        # Assert
        assert err.value == exception_message