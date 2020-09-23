import json

import factory
import pytest


class TestGetTaskDetailsInGroupPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters.get_task_details_in_group_presenter_implementation import \
            GetTaskDetailsInGroupPresenterImplementation
        return GetTaskDetailsInGroupPresenterImplementation()

    @pytest.fixture
    def task_ids(self):
        task_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        return task_ids

    @pytest.fixture
    def stage_ids(self):
        stage_ids = [
            "stage1", "stage2", "stage3", "stage4", "stage5", "stage6",
            "stage7", "stage8", "stage9", "stage10", "stage11", "stage12",
            "stage13", "stage14", "stage15"
        ]
        return stage_ids

    @pytest.fixture
    def task_base_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=15
        )
        return task_base_details_dtos

    @pytest.fixture
    def task_stage_complete_details_dtos(self, task_ids, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            GetTaskStageCompleteDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            StageActionDetailsDTOFactory
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        task_stage_complete_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory.create_batch(
                size=15,
                field_dtos=FieldDetailsDTOFactory.create_batch(size=3),
                stage_id=factory.Iterator(stage_ids),
                action_dtos=StageActionDetailsDTOFactory.create_batch(
                    size=1, stage_id=factory.Iterator(stage_ids)
                )
            )
        return task_stage_complete_details_dtos

    @pytest.fixture
    def task_stage_assignee_details_dto(self, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskStageAssigneeDetailsDTOFactory
        TaskStageAssigneeDetailsDTOFactory.reset_sequence()
        task_stage_assignee_details_dto = \
            TaskStageAssigneeDetailsDTOFactory.create_batch(
                size=15,
                stage_id=factory.Iterator(stage_ids)
            )
        return task_stage_assignee_details_dto

    @pytest.fixture
    def task_complete_details_dto(
            self, task_base_details_dtos, task_stage_complete_details_dtos,
            task_stage_assignee_details_dto
    ):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        task_complete_details_dto = TasksCompleteDetailsDTOFactory(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_details_dtos=task_stage_complete_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_details_dto
        )
        return task_complete_details_dto

    @pytest.fixture()
    def task_ids_and_count_dto(self):
        from ib_adhoc_tasks.interactors.dtos.dtos import TaskIdsAndCountDTO
        task_ids_and_count_dto = TaskIdsAndCountDTO(
            task_ids=[1, 2, 3, 4],
            total_tasks_count=10
        )
        return task_ids_and_count_dto

    def test_get_task_details_in_group_response(
            self, presenter, task_complete_details_dto, task_ids_and_count_dto,
            snapshot
    ):
        # Act
        response = presenter.get_task_details_in_group_response(
            tasks_complete_details_dto=task_complete_details_dto,
            task_ids_and_count_dto=task_ids_and_count_dto
        )

        # Assert
        response_dict = json.loads(response.content)

        snapshot.assert_match(
            name="get_task_details_in_group_response",
            value=response_dict
        )
