from unittest.mock import create_autospec, Mock

import pytest


class TestGetTaskIdsForViewInteractor:

    @pytest.fixture()
    def elastic_storage(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
            ElasticStorageInterface
        elastic_storage = create_autospec(ElasticStorageInterface)
        return elastic_storage

    @pytest.fixture()
    def interactor(self, elastic_storage):
        from ib_adhoc_tasks.interactors.get_task_ids_for_view_interactor import \
            GetTaskIdsForViewInteractor
        interactor = GetTaskIdsForViewInteractor(
            elastic_storage=elastic_storage)
        return interactor

    @pytest.fixture()
    def group_by_dtos(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByDTOFactory
        GroupByDTOFactory.reset_sequence(1)
        group_by_dtos = GroupByDTOFactory.create_batch(2)
        return group_by_dtos

    def test_invalid_project_id_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker):
        # Arrange
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = []

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos
            )
        get_valid_project_ids_mock.assert_called_once_with(
            project_ids=[project_id]
        )

    def test_invalid_task_template_id_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker):
        # Arrange
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_task_template_id_mock, get_valid_project_ids_mock
        from ib_adhoc_tasks.adapters.task_interface import InvalidTaskTemplateId

        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        validate_task_template_id_mock = validate_task_template_id_mock(mocker)
        validate_task_template_id_mock.side_effect = InvalidTaskTemplateId

        # Assert
        with pytest.raises(InvalidTaskTemplateId):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos
            )
        validate_task_template_id_mock.assert_called_once_with(
            task_template_id=adhoc_template_id)

    def test_with_duplicate_orders_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker):
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        for group_by_dto in group_by_dtos:
            group_by_dto.order = 1

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock = validate_task_template_id_mock(mocker)

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            DuplicateGroupByOrder
        with pytest.raises(DuplicateGroupByOrder):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos
            )
        validate_task_template_id_mock.assert_called_once_with(
            task_template_id=adhoc_template_id
        )

    def test_with_valid_details_return_response(
            self, interactor, elastic_storage, group_by_dtos, mocker):
        # Arrange
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock = validate_task_template_id_mock(mocker)

        expected_get_group_details_of_project_mock = Mock()
        elastic_storage.get_group_details_of_project.return_value = \
            expected_get_group_details_of_project_mock

        # Act
        response = interactor.get_task_ids_for_view(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos
        )

        # Assert
        assert response == expected_get_group_details_of_project_mock
        elastic_storage.get_group_details_of_project.assert_called_once_with(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos
        )
