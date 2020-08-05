import factory
import pytest

from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    GoFRoleFactory, FieldFactory
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory,
    GoFRolesDTOFactory,
    CompleteGoFDetailsDTOFactory,
    FieldCompleteDetailsDTOFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence(1)
        TaskTemplateFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        FieldCompleteDetailsDTOFactory.reset_sequence(1)

    def test_get_valid_template_ids_in_given_template_ids(self, storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_ids = [task_template.template_id, "FIN_VENDOR"]
        expected_valid_template_ids = [task_template.template_id]

        # Act
        actual_valid_template_ids = \
            storage.get_valid_template_ids_in_given_template_ids(template_ids)

        # Assert
        assert expected_valid_template_ids == actual_valid_template_ids

    def test_get_field_details_for_given_field_ids(self, storage):
        # Arrange
        field_objects = FieldFactory.create_batch(size=2)
        field_ids_list = [field_object.field_id for field_object in
                          field_objects]
        field_types_list = [
            field_object.field_type for field_object in field_objects
        ]
        field_required_list = [
            field_object.required for field_object in field_objects
        ]
        field_values_list = [
            field_object.field_values for field_object in field_objects
        ]
        allowed_formats_list = [
            field_object.allowed_formats for field_object in field_objects
        ]
        validation_regex_list = [
            field_object.validation_regex for field_object in field_objects
        ]
        expected_field_type_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=2, field_id=factory.Iterator(field_ids_list),
            field_type=factory.Iterator(field_types_list),
            required=factory.Iterator(field_required_list),
            field_values=factory.Iterator(field_values_list),
            allowed_formats=factory.Iterator(allowed_formats_list),
            validation_regex=factory.Iterator(validation_regex_list)
        )

        # Act
        actual_field_type_dtos = storage.get_field_details_for_given_field_ids(
            field_ids=field_ids_list
        )

        # Assert
        assert expected_field_type_dtos == actual_field_type_dtos

    def test_check_is_template_exists_with_valid_template_id_returns_true(self,
                                                                          storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_id = task_template.template_id
        expected_response = True

        # Act
        actual_response = storage.check_is_template_exists(template_id)

        # Assert
        assert expected_response == actual_response
