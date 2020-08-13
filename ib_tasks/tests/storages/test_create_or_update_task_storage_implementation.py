import factory
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.models import Task, TaskGoF, TaskGoFField
from ib_tasks.tests.factories.models import GoFRoleFactory, FieldRoleFactory, \
    TaskFactory, FieldFactory, TaskGoFFactory, TaskGoFFieldFactory, GoFFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFFieldDTOFactory, \
    TaskGoFWithTaskIdDTOFactory
from ib_tasks.tests.factories.interactor_dtos import CreateTaskDTOFactory


@pytest.mark.django_db
class TestCreateOrUpdateTaskStorageImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskGoFWithTaskIdDTOFactory.reset_sequence()
        TaskFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.create_or_update_task_storage_implementation \
            import CreateOrUpdateTaskStorageImplementation
        storage = CreateOrUpdateTaskStorageImplementation()
        return storage

    def test_given_invalid_task_id_raise_exception(self, storage,
                                                   reset_sequence):
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

    def test_given_valid_task_id_returns_task_base_details_dto(
            self, storage, reset_sequence, snapshot):
        # Arrange
        task_id = 1
        task_obj = TaskFactory()
        from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
            TaskBaseDetailsDTO
        excepted_task_base_details_dto = TaskBaseDetailsDTO(
            template_id=task_obj.template_id,
            task_display_id=task_obj.task_display_id,
            title=task_obj.title,
            description=task_obj.description,
            start_date=task_obj.start_date,
            due_date=task_obj.due_date,
            priority=task_obj.priority
        )
        # Act
        actual_task_base_details_dto = storage.validate_task_id(task_id)

        # Assert
        assert actual_task_base_details_dto == excepted_task_base_details_dto

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

    def test_given_task_id_with_no_gof_ids_returns_empty_list(
            self, storage, snapshot
    ):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)

    def test_given_task_gof_ids_returns_task_gof_field_dtos(
            self, storage, snapshot, reset_sequence
    ):
        # Arrange
        gof_objs = GoFFactory.create_batch(size=3)
        task_obj = TaskFactory()
        task_id = task_obj.id
        task_gof_objs = [
            TaskGoFFactory(task_id=task_id, gof=gof_objs[0]),
            TaskGoFFactory(task_id=task_id, gof=gof_objs[1]),
            TaskGoFFactory(task_id=task_id, gof=gof_objs[2])
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
        snapshot.assert_match(name="task_gof_field_dtos",
                              value=task_gof_field_dtos)

    def test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles(
            self, storage, snapshot, reset_sequence
    ):
        # Arrange
        gof_role_objs = GoFRoleFactory.create_batch(size=10)
        gof_role_obj = GoFRoleFactory(role=ALL_ROLES_ID)
        gof_ids = [
            gof_role_objs[0].gof_id,
            gof_role_objs[3].gof_id,
            gof_role_objs[5].gof_id,
            gof_role_objs[9].gof_id,
            gof_role_objs[1].gof_id,
            gof_role_obj.gof_id
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

    def test_given_gof_ids_and_user_roles_not_having_permission_for_gof_ids_but_permission_for_all_roles_returns_gof_ids(
            self, reset_sequence, snapshot, storage
    ):
        # Arrange
        gof_role_objs = GoFRoleFactory.create_batch(size=10)
        gof_role_obj = GoFRoleFactory(role=ALL_ROLES_ID)
        gof_ids = [
            gof_role_objs[0].gof_id,
            gof_role_objs[3].gof_id,
            gof_role_objs[5].gof_id,
            gof_role_objs[9].gof_id,
            gof_role_objs[1].gof_id,
            gof_role_obj.gof_id
        ]
        user_roles = [
            "ADMIN"
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
            self, storage, snapshot, reset_sequence
    ):
        # Arrange
        field_role_objs = FieldRoleFactory.create_batch(size=10)
        field_role_obj = FieldRoleFactory(role=ALL_ROLES_ID)
        field_ids = [
            field_role_objs[0].field_id,
            field_role_objs[3].field_id,
            field_role_objs[9].field_id,
            field_role_objs[6].field_id,
            field_role_obj.field_id
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
            name="field_ids_having_permission",
            value=field_ids_having_permission
        )

    def test_given_field_ids_and_user_roles_not_having_permission_for_field_ids_but_permission_for_all_roles_returns_field_ids(
            self, reset_sequence, snapshot, storage
    ):
        # Arrange
        field_role_objs = FieldRoleFactory.create_batch(size=10)
        field_role_obj = FieldRoleFactory(role=ALL_ROLES_ID)
        field_ids = [
            field_role_objs[0].field_id,
            field_role_objs[3].field_id,
            field_role_objs[9].field_id,
            field_role_objs[6].field_id,
            field_role_obj.field_id
        ]
        user_roles = [
            "ADMIN"
        ]

        # Act
        field_ids_having_permission = storage.get_field_ids_having_permission(
            field_ids=field_ids, user_roles=user_roles
        )

        # Assert
        snapshot.assert_match(
            name="field_ids_having_permission",
            value=field_ids_having_permission
        )

    def test_create_task_with_template_id(self, storage, reset_sequence):
        # Arrange
        from ib_tasks.constants.constants import TASK_DISPLAY_ID
        create_task_dto = CreateTaskDTOFactory()
        expected_task_display_id = TASK_DISPLAY_ID.format(1)

        # Act
        created_task_id = \
            storage.create_task_with_given_task_details(create_task_dto)

        # Assert
        import datetime
        from ib_tasks.constants.config import TIME_FORMAT
        due_date_time = datetime.datetime.combine(
            create_task_dto.due_date,
            datetime.datetime.strptime(create_task_dto.due_time,
                                       TIME_FORMAT).time()
        )
        task = Task.objects.get(id=created_task_id)
        assert task.template_id == create_task_dto.task_template_id
        assert task.created_by == create_task_dto.created_by_id
        assert task.title == create_task_dto.title
        assert task.description == create_task_dto.description
        assert task.start_date.date() == create_task_dto.start_date
        assert task.due_date == due_date_time
        assert task.priority == create_task_dto.priority
        assert task.task_display_id == expected_task_display_id

    def test_create_task_gofs(self, storage, reset_sequence):
        # Arrange
        gof_obj = GoFFactory()
        task = TaskFactory()

        task_gof_dtos = TaskGoFWithTaskIdDTOFactory.create_batch(
            size=1, task_id=task.id, gof_id=gof_obj.gof_id
        )

        # Act
        task_gof_details_dtos = storage.create_task_gofs(task_gof_dtos)

        # Assert
        for task_gof_dto in task_gof_dtos:
            TaskGoF.objects.get(
                task_id=task_gof_dto.task_display_id,
                gof_id=task_gof_dto.gof_id,
                same_gof_order=task_gof_dto.same_gof_order
            )
        for task_gof_details_dto in task_gof_details_dtos:
            task_gof_object = TaskGoF.objects.get(
                id=task_gof_details_dto.task_gof_id
            )
            assert task_gof_object.gof_id == task_gof_details_dto.gof_id
            assert (
                    task_gof_object.same_gof_order ==
                    task_gof_details_dto.same_gof_order
            )

    def test_create_task_gof_fields(self, storage, reset_sequence):

        # Arrange

        task_gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=1)
        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        task_gof_ids = [
            task_gof_field_dto.task_gof_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        FieldFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids)
        )
        TaskGoFFactory.create_batch(
            size=1, id=factory.Iterator(task_gof_ids)
        )

        # Act
        storage.create_task_gof_fields(task_gof_field_dtos)

        # Assert
        for task_gof_field_dto in task_gof_field_dtos:
            TaskGoFField.objects.get(
                field_id=task_gof_field_dto.field_id,
                field_response=task_gof_field_dto.field_response,
                task_gof_id=task_gof_field_dto.task_gof_id
            )

    def test_get_gof_ids_related_to_a_task(self, storage, reset_sequence):

        # Arrange
        task_id = 1

        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id
        )
        expected_task_gof_dtos = [
            GoFIdWithSameGoFOrderDTO(
                gof_id=task_gof.gof_id,
                same_gof_order=task_gof.same_gof_order
            )
            for task_gof in task_gofs
        ]

        # Act
        actual_task_gof_dtos = \
            storage.get_gof_ids_with_same_gof_order_related_to_a_task(
                task_id)

        # Assert
        assert expected_task_gof_dtos == actual_task_gof_dtos

    def test_get_field_ids_related_to_given_task(self, storage,
                                                 reset_sequence):

        # Arrange
        task_id = 1

        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id
        )
        task_gof_fields = TaskGoFFieldFactory.create_batch(
            size=2, task_gof=factory.Iterator(task_gofs)
        )
        from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
        expected_fields_dtos = [
            FieldIdWithTaskGoFIdDTO(
                field_id=task_gof_field.field_id,
                task_gof_id=task_gof_field.task_gof_id
            )
            for task_gof_field in task_gof_fields
        ]

        # Act
        actual_fields_dtos = \
            storage.get_field_ids_with_task_gof_id_related_to_given_task(
                task_id)

        # Assert
        assert expected_fields_dtos == actual_fields_dtos

    def test_update_task_gofs(self, storage, reset_sequence):

        # Arrange
        task_id = 1

        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id
        )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTOFactory(
                task_id=task_gof.task_display_id,
                gof_id=task_gof.gof_id,
                same_gof_order=2
            )
            for task_gof in task_gofs
        ]

        # Act
        task_gof_details_dtos = storage.update_task_gofs(task_gof_dtos)

        # Arrange
        for task_gof_dto in task_gof_dtos:
            TaskGoF.objects.get(
                task_id=task_gof_dto.task_id,
                gof_id=task_gof_dto.gof_id,
                same_gof_order=task_gof_dto.same_gof_order
            )
        for task_gof_details_dto in task_gof_details_dtos:
            task_gof_object = TaskGoF.objects.get(
                id=task_gof_details_dto.task_gof_id
            )
            assert task_gof_object.gof_id == task_gof_details_dto.gof_id
            assert (
                    task_gof_object.same_gof_order ==
                    task_gof_details_dto.same_gof_order
            )

    def test_update_task_gof_fields(self, storage, reset_sequence):

        # Arrange

        task_gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(
            size=1, field_response=factory.Iterator(["field_response"])
        )
        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        task_gof_ids = [
            task_gof_field_dto.task_gof_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        fields = FieldFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids)
        )
        task_gofs = TaskGoFFactory.create_batch(
            size=1, id=factory.Iterator(task_gof_ids)
        )
        TaskGoFFieldFactory.create_batch(
            size=1, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        # Act
        storage.update_task_gof_fields(task_gof_field_dtos)

        # Assert
        for task_gof_field_dto in task_gof_field_dtos:
            TaskGoFField.objects.get(
                field_id=task_gof_field_dto.field_id,
                field_response=task_gof_field_dto.field_response,
                task_gof_id=task_gof_field_dto.task_gof_id
            )

    def test_is_valid_task_id_with_valid_task_id(self, storage,
                                                 reset_sequence):

        # Arrange
        task = TaskFactory.create()
        task_id = task.id
        expected_response = True

        # Act
        actual_response = storage.is_valid_task_id(task_id)

        # Assert
        assert actual_response == expected_response

    def test_is_valid_task_id_with_invalid_task_id(self, storage,
                                                   reset_sequence):

        # Arrange
        TaskFactory.create_batch(size=5)
        task_id = 100
        expected_response = False

        # Act
        actual_response = storage.is_valid_task_id(task_id)

        # Assert
        assert actual_response == expected_response
