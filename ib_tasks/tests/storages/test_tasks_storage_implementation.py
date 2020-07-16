import factory
import pytest

from ib_tasks.models.gof_role import GoFRole
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory
from ib_tasks.tests.factories.storage_dtos import GoFRoleDTOFactory


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    def test_get_existing_gof_ids_in_given_gof_ids(self, storage):
        # Arrange
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = ["FIN_REQUEST_DETAILS", "FIN_BANK_DETAILS"]
        expected_existing_gof_ids = ["FIN_REQUEST_DETAILS"]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_get_valid_field_ids_in_given_field_ids(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import FieldFactory
        fields = FieldFactory.create_batch(size=2)
        field_ids = ["FIN_PAYMENT_REQUESTOR", "FIN_PAYMENT_APPROVER"]
        expected_valid_field_ids = ["FIN_PAYMENT_REQUESTOR"]

        # Act
        actual_valid_field_ids = \
            storage.get_valid_field_ids_in_given_field_ids(field_ids=field_ids)

        # Assert
        assert expected_valid_field_ids == actual_valid_field_ids

    def test_create_gofs(self, storage):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        task_templates = TaskTemplateFactory.create_batch(size=2)

        gof_dtos = [
            GoFDTOFactory(task_template_id=task_templates[0].pk),
            GoFDTOFactory(task_template_id=task_templates[0].pk)
        ]

        # Act
        storage.create_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.order == gof_dto.order
            assert gof.max_columns == gof_dto.max_columns
            assert gof.task_template_id == gof_dto.task_template_id

    def test_create_gof_roles(self, storage):

        # Arrange
        gof_role_dtos = [
            GoFRoleDTOFactory(), GoFRoleDTOFactory()
        ]
        gof_ids = [
            gof_role_dto.gof_id
            for gof_role_dto in gof_role_dtos
        ]
        GoFFactory.create_batch(size=2, gof_id=factory.Iterator(gof_ids))

        # Act
        storage.create_gof_roles(gof_role_dtos=gof_role_dtos)

        # Assert
        for gof_role_dto in gof_role_dtos:
            gof_role = GoFRole.objects.get(
                gof_id=gof_role_dto.gof_id, role=gof_role_dto.role
            )
            assert gof_role_dto.permission_type == gof_role.permission_type

    def test_create_gof_fields(self, storage):

        # Arrange
        from ib_tasks.models.field import Field
        from ib_tasks.tests.factories.storage_dtos import GoFFieldDTOFactory
        from ib_tasks.tests.factories.models import FieldFactory
        gof_field_dtos = GoFFieldDTOFactory.create_batch(size=2)
        field_ids = [
            gof_field_dto.field_id
            for gof_field_dto in gof_field_dtos
        ]
        FieldFactory.create_batch(size=2, field_id=factory.Iterator(field_ids))
        gof_ids = [
            gof_field_dto.gof_id
            for gof_field_dto in gof_field_dtos
        ]
        GoFFactory.create_batch(size=2, gof_id=factory.Iterator(gof_ids))

        # Act
        storage.create_gof_fields(gof_field_dtos=gof_field_dtos)

        # Assert
        for gof_field_dto in gof_field_dtos:
            field = Field.objects.get(pk=gof_field_dto.field_id)
            assert field.gof_id == gof_field_dto.gof_id
