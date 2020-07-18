import factory
import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    GoFRoleFactory
from ib_tasks.tests.factories.storage_dtos import GoFRoleDTOFactory, \
    GoFRoleWithIdDTOFactory


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

    def test_get_valid_template_ids_in_given_template_ids(self, storage):

        # Arrange
        task_template = TaskTemplateFactory()
        template_ids = ["FIN_PR", "FIN_VENDOR"]
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

        pr_task_template = TaskTemplateFactory.create(
            template_id="FIN_PR", name="Payment Request"
        )
        vendor_task_template = TaskTemplateFactory.create(
            template_id="FIN_VENDOR", name="Vendor"
        )
        gofs = [
            GoFFactory(
                display_name="Request Details",
                task_template=vendor_task_template,
                order=1,
                max_columns=3
            ),
            GoFFactory(
                display_name="Vendor Type",
                task_template=pr_task_template,
                order=2,
                max_columns=4
            )
        ]

        gof_dtos = [
            GoFDTOFactory(
                gof_id=gofs[0].gof_id,
                gof_display_name="details of request",
                task_template_id=pr_task_template.template_id,
                order=10,
                max_columns=12
            ),
            GoFDTOFactory(
                gof_id=gofs[1].gof_id,
                gof_display_name="details of vendor",
                task_template_id=vendor_task_template.template_id,
                order=10,
                max_columns=12
            )
        ]

        # Act
        storage.update_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.order == gof_dto.order
            assert gof.max_columns == gof_dto.max_columns
            assert gof.task_template_id == gof_dto.task_template_id

    def test_update_gof_roles(self, storage):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_role_with_id_dtos = [
            GoFRoleWithIdDTOFactory(
                id=gof_role.id,
                gof_id=gof_role.gof_id,
                role=gof_role.role,
                permission_type=PermissionTypes.WRITE.value
            )
            for gof_role in gof_roles
        ]

        # Act
        storage.update_gof_roles(gof_role_with_id_dtos=gof_role_with_id_dtos)

        # Assert
        for gof_role_with_id_dto in gof_role_with_id_dtos:
            gof_role = GoFRole.objects.get(
                gof_id=gof_role_with_id_dto.gof_id,
                role=gof_role_with_id_dto.role
            )
            assert gof_role_with_id_dto.permission_type == \
                   gof_role.permission_type

    def test_get_roles_for_given_gof_ids(self, storage):

        # Arrange
        gof_roles = GoFRoleFactory.create_batch(size=2)
        gof_ids = [gof_role.gof_id for gof_role in gof_roles]

        # Act
        actual_gof_role_with_id_dtos = \
            storage.get_roles_for_given_gof_ids(gof_ids=gof_ids)

        # Assert
        for gof_role_with_id_dto in actual_gof_role_with_id_dtos:
            for gof_role in gof_roles:
                if gof_role.id == gof_role_with_id_dto.id:
                    assert gof_role.gof_id == gof_role_with_id_dto.gof_id
                    assert gof_role.role == gof_role_with_id_dto.role
                    assert gof_role.permission_type == \
                           gof_role_with_id_dto.permission_type

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
                    assert gof.task_template_id == gof_dto.task_template_id
                    assert gof.order == gof_dto.order
                    assert gof.max_columns == gof_dto.max_columns
                    assert gof.enable_multiple_gofs == gof_dto.enable_multiple_gofs
