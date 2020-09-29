"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""

import pytest

from ib_tasks.interactors.get_task_ids_interactor import GetTaskIdsInteractor, \
    InvalidLimitValue, InvalidOffsetValue
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, TaskIdsDTO


class TestGetTaskIdsInteractor:

    @pytest.fixture
    def stage_storage(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        import unittest.mock
        return unittest.mock.create_autospec(StageStorageInterface)

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        import unittest.mock
        return unittest.mock.create_autospec(TaskStorageInterface)

    @pytest.fixture
    def elasticsearch_storage(self):
        from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
            ElasticSearchStorageInterface
        import unittest.mock
        return unittest.mock.create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def filter_storage(self):
        import unittest.mock
        from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
            FilterStorageInterface
        return unittest.mock.create_autospec(FilterStorageInterface)

    @pytest.fixture
    def field_storage(self):
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
            FieldsStorageInterface
        return create_autospec(FieldsStorageInterface)

    def test_with_invalid_stage_ids_raise_error(
            self, task_storage, stage_storage,
            elasticsearch_storage, filter_storage, field_storage):
        # Arrange
        stage_ids = [['STAGE_ID_1', 'STAGE_ID_2'],
                     ['STAGE_ID_3', 'STAGE_ID_4']]

        valid_stage_ids = ['STAGE_ID_3', 'STAGE_ID_4']
        interactor = GetTaskIdsInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage,
            field_storage=field_storage
        )
        task_config_dtos = [
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[0],
                offset=0,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            ),
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[1],
                offset=0,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            )
        ]
        stage_storage.get_existing_stage_ids.return_value = valid_stage_ids

        # Act
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        with pytest.raises(InvalidStageIdsListException) as error:
            interactor.get_task_ids(task_details_configs=task_config_dtos)

    def test_with_invalid_limit_raise_error(
            self, task_storage, stage_storage, elasticsearch_storage,
            filter_storage, field_storage):
        # Arrange
        stage_ids = [['STAGE_ID_1', 'STAGE_ID_2'],
                     ['STAGE_ID_3', 'STAGE_ID_4']]
        stage_ids_single_list = ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3',
                                 'STAGE_ID_4']
        interactor = GetTaskIdsInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage,
            field_storage=field_storage
        )
        task_config_dtos = [
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[0],
                offset=0,
                limit=-2,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            ),
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[1],
                offset=0,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            )
        ]
        stage_storage.get_existing_stage_ids.return_value = stage_ids_single_list
        # Act

        with pytest.raises(InvalidLimitValue) as error:
            interactor.get_task_ids(task_details_configs=task_config_dtos)

    def test_with_invalid_offset_raise_error(
            self, task_storage, stage_storage, elasticsearch_storage,
            filter_storage, field_storage):
        # Arrange
        stage_ids = [['STAGE_ID_1', 'STAGE_ID_2'],
                     ['STAGE_ID_3', 'STAGE_ID_4']]
        stage_ids_single_list = ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3',
                                 'STAGE_ID_4']
        interactor = GetTaskIdsInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage,
            field_storage=field_storage
        )
        task_config_dtos = [
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[0],
                offset=3,
                limit=2,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            ),
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[1],
                offset=-3,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            )
        ]
        stage_storage.get_existing_stage_ids.return_value = stage_ids_single_list
        # Act

        with pytest.raises(InvalidOffsetValue) as error:
            interactor.get_task_ids(task_details_configs=task_config_dtos)

    def test_with_valid_stage_ids_return_task_ids_with_stage_ids_dict(
            self, stage_storage, task_storage, snapshot, field_storage,
            elasticsearch_storage, filter_storage, mocker):
        # Arrange
        from ib_tasks.tests.factories.storage_dtos import \
            TaskStageIdsDTOFactory
        expected_response = [
            TaskStageIdsDTOFactory.create_batch(4, stage_id='STAGE_ID_1') +
            TaskStageIdsDTOFactory.create_batch(4, stage_id='STAGE_ID_2'),
            TaskStageIdsDTOFactory.create_batch(4, stage_id='STAGE_ID_3') +
            TaskStageIdsDTOFactory.create_batch(4, stage_id='STAGE_ID_4'),

        ]
        stage_ids = [['STAGE_ID_1', 'STAGE_ID_2'],
                     ['STAGE_ID_3', 'STAGE_ID_4']]
        stage_ids_single_list = ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3',
                                 'STAGE_ID_4']
        task_config_dtos = [
            TaskDetailsConfigDTO(
                unique_key='1',
                stage_ids=stage_ids[0],
                offset=0,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            ),
            TaskDetailsConfigDTO(
                unique_key="1",
                stage_ids=stage_ids[1],
                offset=0,
                limit=5,
                search_query="hello",
                user_id='user_id_1',
                project_id='FIN_MAN'
            )
        ]
        task_ids_dtos = [
            TaskIdsDTO(
                unique_key="1",
                task_stage_ids=expected_response[0],
                total_tasks=100
            ),
            TaskIdsDTO(
                unique_key="1",
                task_stage_ids=expected_response[1],
                total_tasks=100
            )
        ]
        from unittest.mock import call
        calls = (call(stage_ids=stage_ids[0], offset=0, limit=5),
                 call(stage_ids=stage_ids[1], offset=0, limit=5))
        interactor = GetTaskIdsInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage,
            field_storage=field_storage
        )
        stage_storage.get_existing_stage_ids.return_value = stage_ids_single_list
        elasticsearch_storage.filter_tasks_with_stage_ids.side_effect = [
            (expected_response[0], 100), (expected_response[1], 100)
        ]

        # Act
        actual_response = interactor.get_task_ids(
            task_details_configs=task_config_dtos
        )

        # Assert

        elasticsearch_storage.filter_tasks_with_stage_ids.assert_called_once_with(
            stage_ids=stage_ids_single_list
        )
        snapshot.assert_match(actual_response, 'response')
