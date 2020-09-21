import factory
import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, \
    StagePermittedRolesFactory


@pytest.mark.django_db
class TestGetUserPermittedStageIds:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

    def test_when_user_permitted_stages_exists_returns_stage_ids(self, snapshot):
        # Arrange
        stage_ids = [1, 2]
        user_roles = ["role_1", "role_2"]

        stages = StageModelFactory.create_batch(size=2)
        StagePermittedRolesFactory.create_batch(
            size=2, stage=factory.Iterator(stages),
            role_id=factory.Iterator(user_roles))

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_user_permitted_stage_ids(
            stage_ids=stage_ids, roles=user_roles)

        # Assert
        snapshot.assert_match(response, "user_permitted_stage_ids")

    def test_when_user_permitted_stages_not_exists_returns_empty_stage_ids(
            self, snapshot):
        # Arrange
        stage_ids = [1, 2]
        user_roles = ["role_1", "role_2"]

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_user_permitted_stage_ids(
            stage_ids=stage_ids, roles=user_roles)

        # Assert
        snapshot.assert_match(response, "user_permitted_stage_ids")

    def test_when_user_permitted_stages_exists_with_all_role_ids_returns_stage_ids(
            self, snapshot):
        # Arrange
        stage_ids = [1, 2]
        user_roles = ["role_1", "role_2"]

        import factory
        from ib_tasks.tests.factories.models import StageModelFactory, \
            StagePermittedRolesFactory

        StageModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

        from ib_tasks.constants.constants import ALL_ROLES_ID

        stages = StageModelFactory.create_batch(size=2)
        StagePermittedRolesFactory.create_batch(
            size=2, stage=factory.Iterator(stages),
            role_id=ALL_ROLES_ID)

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_user_permitted_stage_ids(
            stage_ids=stage_ids, roles=user_roles)

        # Assert
        snapshot.assert_match(response, "user_permitted_stage_ids")
