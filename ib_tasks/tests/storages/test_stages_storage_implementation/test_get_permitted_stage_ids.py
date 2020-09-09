import pytest

from ib_tasks.tests.factories.models import StageModelFactory, \
    ProjectTaskTemplateFactory, StagePermittedRolesFactory


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence(1)
        ProjectTaskTemplateFactory.reset_sequence()

    def test_get_stage_actions(self):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        project_id = "project_1"
        project_task_template = ProjectTaskTemplateFactory.create(
            project_id=project_id)
        template_id = project_task_template.task_template.template_id
        StagePermittedRolesFactory.create_batch(
            size=3, role_id='ROLE_1', stage__task_template_id=template_id)
        storage = StagesStorageImplementation()
        user_roles = ["ROLE_1", "ROLE_2", "ROLE_3"]

        # Act
        result = storage.get_permitted_stage_ids(
            user_roles, project_id=project_id)

        # Assert
        assert result == ['stage_id_0', 'stage_id_1', 'stage_id_2']

    def test_returns_empty_stage_roles(self):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        user_roles = ["ROLE_1", "ROLE_2", "ROLE_3"]
        expected = []
        # Act
        result = storage.get_permitted_stage_ids(user_roles, project_id=None)

        # Assert
        assert result == expected
