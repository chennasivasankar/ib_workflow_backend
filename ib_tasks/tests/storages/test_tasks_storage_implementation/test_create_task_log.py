import datetime

import freezegun
import pytest


@pytest.mark.django_db
class TestCreateTaskLog:

    @freezegun.freeze_time(datetime.datetime(2020, 8, 1, 7, 4, 3))
    def test_create_task_log_with_valid_details(self, storage):
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
        storage.create_task_log(create_task_log_dto=create_task_log_dto)

        # Assert
        from ib_tasks.models.task_log import TaskLog
        task_log = TaskLog.objects.get(id=expected_task_log_id)

        assert task_log.id == expected_task_log_id
        assert task_log.task_json == expected_task_json
        assert task_log.action_id == expected_action_id
        assert task_log.user_id == expected_user_id
        assert task_log.task_id == expected_task_id
        assert task_log.acted_at.replace(tzinfo=None) == expected_acted_at
