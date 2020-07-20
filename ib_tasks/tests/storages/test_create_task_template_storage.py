import pytest
from ib_tasks.tests.factories.models import TaskTemplateFactory

@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()

    @pytest.mark.django_db
    def test_check_is_template_exists_with_invalid_template_id_returns_false(
            self, storage):
        #Arrange
        template_id = "Template_1"

        #Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        #Assert
        assert is_template_exists is False

    @pytest.mark.django_db
    def test_check_is_template_exists_with_valid_template_id_returns_true(
            self, storage):
        #Arrange
        task_template = TaskTemplateFactory()
        template_id = task_template.template_id

        #Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        #Assert
        assert is_template_exists is True

    @pytest.mark.django_db
    def test_get_task_template_name(self, storage):
        #Arrange
        task_template = TaskTemplateFactory()
        template_id = task_template.template_id
        expected_template_name = task_template.name

        #Act
        template_name = \
            storage.get_task_template_name(template_id=template_id)

        #Assert
        assert template_name == expected_template_name

    @pytest.mark.django_db
    def test_create_task_template(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        template_name = "Task Template 1"

        #Act
        storage.create_task_template(
            template_id=template_id, template_name=template_name
        )

        #Assert
        from ib_tasks.models.task_template import TaskTemplate
        task_template = TaskTemplate.objects.get(template_id=template_id)

        assert task_template.template_id == template_id
        assert task_template.name == template_name

    @pytest.mark.django_db
    def test_update_task_template(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        template_name = "iB Template"
        TaskTemplateFactory(template_id=template_id, name=template_name)

        #Act
        storage.update_task_template(
            template_id=template_id, template_name=template_name
        )

        #Assert
        from ib_tasks.models.task_template import TaskTemplate
        task_template = TaskTemplate.objects.get(template_id=template_id)

        assert task_template.template_id == template_id
        assert task_template.name == template_name
