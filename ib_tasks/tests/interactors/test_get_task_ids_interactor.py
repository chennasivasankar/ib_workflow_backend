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

    @pytest.fixture()
    def task_condition_mock(self, mocker):
        path = 'ib_tasks.interactors.get_task_details_conditions_dtos' \
               '.GetConditionsForTaskDetails'
        mock_obj = mocker.patch(path)
        return mock_obj
