import pytest
from ib_tasks.tests.factories.models import (
    TaskFactory,
    TaskGoFFactory,
    TaskGoFFieldFactory,
    GoFRoleFactory,
    FieldRoleFactory
)


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

    def test_given_task_id_returns_task_gof_dtos(self, storage, snapshot):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id
        TaskGoFFactory(task_id=task_id)
        TaskGoFFactory(task_id=task_id)
        TaskGoFFactory(task_id=task_id)

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)

    def test_given_task_gof_ids_returns_task_gof_field_dtos(self, storage, snapshot):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id
        task_gof_objs = [
            TaskGoFFactory(task_id=task_id),
            TaskGoFFactory(task_id=task_id),
            TaskGoFFactory(task_id=task_id)
        ]
        TaskGoFFieldFactory(task_gof=task_gof_objs[0])
        TaskGoFFieldFactory(task_gof=task_gof_objs[1])
        TaskGoFFieldFactory(task_gof=task_gof_objs[2])
        TaskGoFFieldFactory(task_gof=task_gof_objs[1])
        TaskGoFFieldFactory(task_gof=task_gof_objs[0])
        task_gof_ids = [
            task_gof_obj.id
            for task_gof_obj in task_gof_objs
        ]

        # Act
        task_gof_field_dtos = storage.get_task_gof_field_dtos(task_gof_ids)

        # Assert
        snapshot.assert_match(name="task_gof_field_dtos", value=task_gof_field_dtos)

    def test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles(
            self, storage, snapshot
    ):
        # Arrange
        gof_role_objs = GoFRoleFactory.create_batch(size=10)
        gof_ids = [
            gof_role_objs[0].gof_id,
            gof_role_objs[3].gof_id,
            gof_role_objs[5].gof_id,
            gof_role_objs[9].gof_id,
            gof_role_objs[1].gof_id
        ]
        user_roles = [
            gof_role_objs[3].role,
            gof_role_objs[9].role,
            gof_role_objs[1].role
        ]

        # Act
        gof_ids_having_permission = storage.get_gof_ids_having_permission(
            gof_ids=gof_ids, user_roles=user_roles
        )

        # Assert
        snapshot.assert_match(
            name="gof_ids_having_permission", value=gof_ids_having_permission
        )

    def test_given_field_ids_and_user_roles_returns_field_ids_having_permission_for_roles(
            self, storage, snapshot
    ):
        # Arrange
        field_role_objs = FieldRoleFactory.create_batch(size=10)
        field_ids = [
            field_role_objs[0].field_id,
            field_role_objs[3].field_id,
            field_role_objs[9].field_id,
            field_role_objs[6].field_id
        ]
        user_roles = [
            field_role_objs[0].role
        ]

        # Act
        field_ids_having_permission = storage.get_field_ids_having_permission(
            field_ids=field_ids, user_roles=user_roles
        )

        # Assert
        snapshot.assert_match(
            name="field_ids_having_permission", value=field_ids_having_permission
        )
