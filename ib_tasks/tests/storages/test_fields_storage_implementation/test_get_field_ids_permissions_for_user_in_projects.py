import factory
import pytest

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskProjectRolesDTO
from ib_tasks.tests.factories.models import FieldFactory, FieldRoleFactory, \
    TaskGoFFactory, TaskGoFFieldFactory


@pytest.mark.django_db
class TestGetFieldIdsPermissionsForUserInProjects:

    def test_get_field_ids_having_permission_for_user_projects(self, storage):
        # Arrange
        user_roles = [
            TaskProjectRolesDTO(
                task_id=1, project_id="project_id_1", roles=["FIN_MAN"]),
            TaskProjectRolesDTO(
                task_id=1, project_id="project_id_1", roles=["FIN_MAN"])]
        fields = FieldFactory.create_batch(size=2)
        FieldRoleFactory.create_batch(
            size=2, permission_type=PermissionTypes.READ.value,
            role=factory.Iterator(user_roles[0].roles),
            field=factory.Iterator(fields)
        )

        gofs = TaskGoFFactory.create_batch(size=3)
        TaskGoFFieldFactory.create_batch(
            size=3, task_gof=factory.Iterator(gofs),
            field=factory.Iterator(fields))

        field_ids = ['FIELD_ID-1', 'FIELD_ID-2']

        # Act
        field_ids_having_permission_for_user = \
            storage.get_field_ids_permissions_for_user_in_projects(
                field_ids=field_ids, task_project_roles=user_roles)

        # Assert
        assert set(field_ids_having_permission_for_user) == set(field_ids)