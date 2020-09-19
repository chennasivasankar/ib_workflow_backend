import pytest

from ib_tasks.tests.factories.models import StageModelFactory, \
    StagePermittedRolesFactory


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence(1)
        StagePermittedRolesFactory.reset_sequence(1)

    @pytest.fixture()
    def storage(self):
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        return storage

    def expected_response(self):
        from ib_tasks.tests.factories.storage_dtos import StageMinimalDTOFactory
        StageMinimalDTOFactory.reset_sequence(1)

        response = [
            StageMinimalDTOFactory(color="blue", name="name_1"),
            StageMinimalDTOFactory(color="orange", name="name_2"),
            StageMinimalDTOFactory(color="green", name="name_3")
        ]
        return response

    def test_get_user_permitted_stages_in_template(self, storage):

        # Arrange
        template_id = "template_1"
        StagePermittedRolesFactory.create_batch(
            size=3, role_id='ROLE_1',
            stage__task_template_id=template_id
        )
        user_roles = ["ROLE_1", "ROLE_2"]
        expected = self.expected_response()

        # Act
        result = storage.get_user_permitted_stages_in_template(
            user_roles=user_roles, template_id=template_id
        )

        # Assert
        assert result == expected

    def test_returns_empty_stage_roles(self, storage):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ["ROLE_2", "ROLE_3"]
        expected = []

        # Act
        result = storage.get_permitted_stage_ids(user_roles, project_id=None)

        # Assert
        assert result == expected
