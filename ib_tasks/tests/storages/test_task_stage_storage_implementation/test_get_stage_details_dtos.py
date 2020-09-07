import pytest

from ib_tasks.tests.factories.models import StageModelFactory


@pytest.mark.django_db
class TestGetStageDetailsDTOS:

    def test_given_stage_ids_returns_stage_details_dtos(
            self, task_storage, snapshot
    ):
        # Arrange
        stage_ids = [1, 2, 3, 4]
        StageModelFactory.create_batch(size=4)

        # Act
        stage_details_dtos = task_storage.get_stage_details_dtos(
            stage_ids=stage_ids
        )

        # Assert
        snapshot.assert_match(name="stage_details_dto",
                              value=stage_details_dtos)
