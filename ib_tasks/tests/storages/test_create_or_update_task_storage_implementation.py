import pytest
from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestCreateOrUpdateTaskStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.create_or_update_task_storage_implementation \
            import CreateOrUpdateTaskStorageImplementation
        storage = CreateOrUpdateTaskStorageImplementation()
        return storage

    def test_given_invalid_task_id_raise_exception(self, storage):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        task_id = -1

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            storage.validate_task_id(task_id)

        # Assert
        exception_obj = err.value
        assert exception_obj.task_id == task_id

    def test_given_valid_task_id_returns_template_id(self, storage):
        # Arrange
        task_id = 1
        task_obj = TaskFactory()
        excepted_template_id = task_obj.template_id

        # Act
        actual_template_id = storage.validate_task_id(task_id)

        # Assert
        assert excepted_template_id == actual_template_id
