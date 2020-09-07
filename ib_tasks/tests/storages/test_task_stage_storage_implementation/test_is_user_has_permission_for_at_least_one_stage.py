import pytest


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
