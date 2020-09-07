import pytest

from ib_tasks.tests.factories.models import StagePermittedRolesFactory, \
    StageModelFactory


@pytest.mark.django_db
class TestTaskStageStorageImplementation:

    def test_given_stage_ids_and_user_roles_if_user_has_permissions_returns_true(
            self, task_storage
    ):
        # Arrange
        user_roles = ["FIN_PAYMENT_REQUESTER"]
        stage_ids = [1, 2, 4, 5]
        is_user_has_permissions = True
        StagePermittedRolesFactory()

        # Act
        response = task_storage.is_user_has_permission_for_at_least_one_stage(
            stage_ids=stage_ids, user_roles=user_roles
        )

        # Assert
        assert response == is_user_has_permissions

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
