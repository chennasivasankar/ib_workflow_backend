import factory
import pytest


@pytest.mark.django_db
class TestGetStageAssigneeDTOS:

    @pytest.fixture()
    def populate_task_stages_history(self):
        TaskStageHistoryModelFactory.reset_sequence()
        stage_ids = [1, 2, 3, 4]
        TaskStageHistoryModelFactory.create_batch(size=4, task_id=1,
                                                  stage_id=factory.Iterator(
                                                      stage_ids))

    def test_given_task_id_stage_ids_returns_task_stage_assignee_dtos(
            self, task_storage,
            populate_task_stages_history, snapshot
    ):
        # Arrange
        task_id = 1
        stage_ids = [1, 2, 3, 4]

        # Act
        task_stage_assignee_dtos = task_storage.get_stage_assignee_dtos(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        snapshot.assert_match(name="task_stage_assignee_dtos",
                              value=task_stage_assignee_dtos)
