import factory
import pytest

from ib_tasks.models.gof_role import GoFRole
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    GoFRoleFactory, FieldFactory, FieldRoleFactory
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory,
    GoFRolesDTOFactory,
    CompleteGoFDetailsDTOFactory,
    FieldCompleteDetailsDTOFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory, FieldDTOFactory


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

    def test_get_existing_gof_ids_in_given_gof_ids(
            self, storage
    ):
        # Arrange
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        expected_existing_gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids

    def test_create_gofs(self, storage):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        gof_dtos = [GoFDTOFactory(), GoFDTOFactory()]

        # Act
        storage.create_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.max_columns == gof_dto.max_columns

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

    def test_update_gofs(self, storage):

        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)

        gof_dtos = [
            GoFDTOFactory(
                gof_id=gofs[0].gof_id,
                gof_display_name="details of request",
                max_columns=12
            ),
            GoFDTOFactory(
                gof_id=gofs[1].gof_id,
                gof_display_name="details of vendor",
                max_columns=12
            )
        ]

        # Act
        storage.update_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.max_columns == gof_dto.max_columns

    def test_delete_gof_roles(self, storage):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_ids = [gof_role.gof_id for gof_role in gof_roles]

        # Act
        storage.delete_gof_roles(gof_ids=gof_ids)

        # Assert
        gof_roles = list(GoFRole.objects.filter(gof_id__in=gof_ids))
        assert gof_roles == []

    def test_get_gof_dtos_for_given_gof_ids(self, storage):

        # Arrange
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_gof_dtos = storage.get_gof_dtos_for_given_gof_ids(gof_ids)

        # Assert
        for gof_dto in actual_gof_dtos:
            for gof in gofs:
                if gof.gof_id == gof_dto.gof_id:
                    assert gof.display_name == gof_dto.gof_display_name
                    assert gof.max_columns == gof_dto.max_columns

    def test_get_existing_gof_ids_given_gof_ids(self, storage):
        # Arrange
        gof_ids = ["gof0", "gof1", "gof2"]
        GoFFactory(gof_id="gof0")
        GoFFactory(gof_id="gof1")
        expected_existing_gof_ids = ["gof0", "gof1"]

        # Act
        actual_existing_gof_ids = storage.get_existing_gof_ids(gof_ids)

        # Assert

        assert expected_existing_gof_ids == actual_existing_gof_ids

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
