import pytest

from ib_tasks.tests.factories.models import StagePermittedRolesFactory


@pytest.mark.django_db
class TestIsUserHasPermissionForAtLeastOneStage:

    def test_given_stage_ids_and_user_roles_if_user_has_no_permissions_returns_false(
            self, task_storage
    ):
        # Arrange
        user_roles = ["PAYMENT_REQUESTER"]
        stage_ids = [1, 2, 4, 5]
        is_user_has_permissions = False

        # Act
        response = task_storage.is_user_has_permission_for_at_least_one_stage(
            stage_ids=stage_ids, user_roles=user_roles
        )

        # Assert
        assert response == is_user_has_permissions

    def test_given_stage_ids_and_user_roles_if_user_has_permissions_returns_true(
            self, task_storage
    ):
        # Arrange
        user_roles = ["FIN_PAYMENT_REQUESTER"]
        stage_ids = [1, 2, 4, 5]
        is_user_has_permissions = True
        StagePermittedRolesFactory(stage_id=stage_ids[0],
                                   role_id=user_roles[0])

        # Act
        response = task_storage.is_user_has_permission_for_at_least_one_stage(
            stage_ids=stage_ids, user_roles=user_roles
        )

        # Assert
        assert response == is_user_has_permissions
