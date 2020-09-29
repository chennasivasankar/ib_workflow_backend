from unittest.mock import patch, Mock

import pytest

from ib_adhoc_tasks.adapters.task_service import TaskService


class TestGetTaskDetailsInGroupInteractor:

    @pytest.fixture
    def presenter_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.presenter_interfaces. \
            get_task_details_in_group_presenter_interface import \
            GetTaskDetailsInGroupPresenterInterface
        presenter = create_autospec(GetTaskDetailsInGroupPresenterInterface)
        return presenter

    @pytest.fixture
    def storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface \
            import \
            StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def elastic_storage_mock(self):
        from mock import create_autospec
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticStorageInterface
        elastic_storage = create_autospec(ElasticStorageInterface)
        return elastic_storage

    @pytest.fixture()
    def interactor(self, storage_mock, elastic_storage_mock):
        from ib_adhoc_tasks.interactors.get_task_details_in_group_interactor \
            import \
            GetTaskDetailsInGroupInteractor
        interactor = GetTaskDetailsInGroupInteractor(
            storage=storage_mock, elastic_storage=elastic_storage_mock
        )
        return interactor

    @staticmethod
    def get_task_ids_for_groups_mock(mocker):
        mock = mocker.patch(
            "ib_adhoc_tasks.interactors.get_task_ids_for_group_interactor"
            ".GetTaskIdsForGroupInteractor.get_task_ids_for_groups"
        )
        return mock

    @pytest.fixture
    def task_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        return TasksCompleteDetailsDTOFactory()

    @pytest.fixture()
    def get_task_details_in_group_input_dto(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GetTaskDetailsInGroupInputDTOFactory
        get_task_details_in_group_input_dto = \
            GetTaskDetailsInGroupInputDTOFactory(
                group_by_values=["PR_PAYMENT_REQUEST_DRAFTS",
                                 "PR_NEED_CLARIFICATION"]
            )
        return get_task_details_in_group_input_dto

    @pytest.fixture
    def task_with_sub_task_count_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskIdWithSubTasksCountDTOFactory
        return TaskIdWithSubTasksCountDTOFactory.create_batch(size=3)

    @pytest.fixture
    def task_with_completed_sub_task_count_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskIdWithCompletedSubTasksCountDTOFactory
        return TaskIdWithCompletedSubTasksCountDTOFactory.create_batch(size=3)

    @patch.object(TaskService, 'get_completed_sub_tasks_count_for_task_ids')
    @patch.object(TaskService, 'get_sub_tasks_count_task_ids')
    @patch.object(TaskService, "get_task_complete_details_dto")
    def test_with_valid_details_return_response(
            self, task_details_mock, task_with_sub_task_count_mock,
            task_with_completed_sub_task_count_mock,
            presenter_mock, storage_mock, task_with_sub_task_count_dtos,
            elastic_storage_mock, interactor,
            task_with_completed_sub_task_count_dtos,
            get_task_details_in_group_input_dto, mocker, task_details_dtos
    ):
        # Arrange
        from ib_adhoc_tasks.interactors.dtos.dtos import \
            TaskIdsForGroupsParameterDTO
        from ib_adhoc_tasks.interactors.dtos.dtos import GroupByValueDTO
        task_with_sub_task_count_mock.return_value = \
            task_with_sub_task_count_dtos
        task_with_completed_sub_task_count_mock.return_value = \
            task_with_completed_sub_task_count_dtos
        task_ids_for_groups_parameter_dto = TaskIdsForGroupsParameterDTO(
            project_id='project_id_0',
            template_id='ADHOC', user_id='user_0',
            groupby_value_dtos=[
                GroupByValueDTO(
                    group_by_display_name='ASSIGNEE',
                    group_by_value='PR_PAYMENT_REQUEST_DRAFTS'),
                GroupByValueDTO(
                    group_by_display_name='STAGE',
                    group_by_value='PR_NEED_CLARIFICATION'
                )
            ],
            limit=5, offset=0
        )
        from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO
        from ib_adhoc_tasks.constants.enum import ViewType
        task_details_input_dto = TasksDetailsInputDTO(
            task_ids=[1, 2, 3, 4], project_id='project_id_0',
            user_id='user_0', view_type=ViewType.LIST.value
        )

        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        group_by_response_dtos = \
            GroupByResponseDTOFactory.create_batch(size=2)

        storage_mock.get_group_by_dtos.return_value = group_by_response_dtos

        get_task_ids_for_groups_mock = self.get_task_ids_for_groups_mock(
            mocker)
        from ib_adhoc_tasks.interactors.dtos.dtos import TaskIdsAndCountDTO
        get_task_ids_for_groups_mock.return_value = TaskIdsAndCountDTO(
            task_ids=[1, 2, 3, 4],
            total_tasks_count=10
        )
        task_details_mock.return_value = task_details_dtos

        expected_presenter_get_task_details_in_group_response = Mock()

        presenter_mock.get_task_details_in_group_response.return_value = \
            expected_presenter_get_task_details_in_group_response

        # Act
        response = interactor.get_task_details_in_group_wrapper(
            get_task_details_in_group_input_dto
            =get_task_details_in_group_input_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_get_task_details_in_group_response
        storage_mock.get_group_by_dtos.assert_called_once_with(
            user_id=get_task_details_in_group_input_dto.user_id,
            view_type=get_task_details_in_group_input_dto.view_type
        )
        get_task_ids_for_groups_mock.assert_called_once_with(
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto
        )
        task_details_mock.assert_called_once_with(
            task_details_input_dto=task_details_input_dto
        )
        task_with_sub_task_count_mock.assert_called_once()
        task_with_completed_sub_task_count_mock.assert_called_once()
