import json
from datetime import timedelta

import pytest

from ib_tasks.interactors.stages_dtos import TaskStageCompleteDetailsDTO
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import LogDurationDTOFactory


class TestGetTaskPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.get_task_stage_history_presenter_implementation import \
            GetTaskStageHistoryPresenterImplementation
        presenter = GetTaskStageHistoryPresenterImplementation()
        return presenter

    def test_get_task_stages_history(self, presenter, snapshot):

        # Arrnage
        from ib_tasks.tests.factories.storage_dtos import StageMinimalDTOFactory
        StageMinimalDTOFactory.reset_sequence(1)
        LogDurationDTOFactory.reset_sequence(1)
        AssigneeDetailsDTOFactory.reset_sequence(1)
        stage_dtos = StageMinimalDTOFactory.create_batch(1)
        from ib_tasks.tests.factories.storage_dtos import TaskStageHistoryDTOFactory
        TaskStageHistoryDTOFactory.reset_sequence(1)
        task_stage_dtos = [
            TaskStageHistoryDTOFactory(left_at=None, stage_duration=timedelta(days=1))
        ]
        log_dtos = LogDurationDTOFactory.create_batch(1)
        user_dtos = [
            AssigneeDetailsDTOFactory(assignee_id="1")
        ]
        task_stage_details_dto = TaskStageCompleteDetailsDTO(
            stage_dtos=stage_dtos,
            task_stage_dtos=task_stage_dtos,
            log_duration_dtos=log_dtos,
            assignee_details=user_dtos
        )

        # Act
        response_object = presenter.get_task_stages_history_response(
            task_stages_details_dto=task_stage_details_dto
        )
        snapshot.assert_match(
            name="task_stages_history", value=json.loads(response_object.content)
        )