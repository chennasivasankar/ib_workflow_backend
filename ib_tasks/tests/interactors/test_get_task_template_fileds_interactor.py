import pytest


class TestGetTaskTemplatesFieldsInteractor:

    @pytest.fixture
    @staticmethod
    def task_storage(self):

        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from unittest.mock import create_autospec
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    @staticmethod
    def field_storage(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        from unittest.mock import create_autospec
        field_storage = create_autospec(FieldsStorageInterface)
        return field_storage

    def test_return_task_templates_fields_details(
            self, task_storage, field_storage):

        # Arrange
        from ib_tasks.tests.factories.storage_dtos \
            import TaskTemplateDTOFactory, GoFToTaskTemplateDTOFactory
        GoFToTaskTemplateDTOFactory.reset_sequence()
        TaskTemplateDTOFactory.reset_sequence()

        task_templates = TaskTemplateDTOFactory.create_batch(2)
        task_storage.get_task_templates_dto.return_value = task_templates

