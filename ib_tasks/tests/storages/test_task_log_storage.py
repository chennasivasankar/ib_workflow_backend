import pytest
import freezegun
import datetime


@pytest.mark.django_db
class TestCreateTaskLog:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskFactory, \
            StageActionFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            CreateTaskLogDTOFactory

        TaskFactory.reset_sequence(1)
        CreateTaskLogDTOFactory.reset_sequence(1)
        StageActionFactory.reset_sequence(1)

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        task_storage = TasksStorageImplementation()
        return task_storage

    def test_check_is_task_exists_with_valid_task_id_returns_true(
            self, task_storage):
        # Arrange
        task_id = 1
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create()

        # Act
        is_task_exists = task_storage.check_is_task_exists(task_id=task_id)

        # Assert
        assert is_task_exists is True

    def test_check_is_task_exists_with_invalid_task_id_returns_false(
            self, task_storage):
        # Arrange
        task_id = 1

        # Act
        is_task_exists = task_storage.check_is_task_exists(task_id=task_id)

        # Assert
        assert is_task_exists is False

    @freezegun.freeze_time(datetime.datetime(2020, 8, 1, 7, 4, 3))
    def test_create_task_log_with_valid_details(self, task_storage):
        # Arrange
        from ib_tasks.tests.factories.models import TaskFactory, \
            StageActionFactory
        TaskFactory.create()
        StageActionFactory.create()

        from ib_tasks.tests.factories.interactor_dtos import \
            CreateTaskLogDTOFactory
        create_task_log_dto = CreateTaskLogDTOFactory.create()

        expected_task_log_id = 1
        expected_task_json = create_task_log_dto.task_json
        expected_action_id = create_task_log_dto.action_id
        expected_user_id = create_task_log_dto.user_id
        expected_task_id = create_task_log_dto.task_id
        expected_acted_at = datetime.datetime(2020, 8, 1, 7, 4, 3)

        # Act
        task_storage.create_task_log(create_task_log_dto=create_task_log_dto)

        # Assert
        from ib_tasks.models.task_log import TaskLog
        task_log = TaskLog.objects.get(id=expected_task_log_id)

        assert task_log.id == expected_task_log_id
        assert task_log.task_json == expected_task_json
        assert task_log.action_id == expected_action_id
        assert task_log.user_id == expected_user_id
        assert task_log.task_id == expected_task_id
        assert task_log.acted_at.replace(tzinfo=None) == expected_acted_at
