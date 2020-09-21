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

    @pytest.fixture()
    def task_offset_and_limit_values_dto(self):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            TaskOffsetAndLimitValuesDTOFactory
        task_offset_and_limit_values_dto = TaskOffsetAndLimitValuesDTOFactory()
        return task_offset_and_limit_values_dto

    def test_invalid_project_id_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        # Arrange
        user_id = "USER_1"
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
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        get_valid_project_ids_mock.assert_called_once_with(
            project_ids=[project_id]
        )

    def test_invalid_task_template_id_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        # Arrange
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_task_template_id_mock, get_valid_project_ids_mock

        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        validate_task_template_id_mock = validate_task_template_id_mock(mocker)
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidTaskTemplateId
        validate_task_template_id_mock.side_effect = InvalidTaskTemplateId

        # Assert
        with pytest.raises(InvalidTaskTemplateId):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        validate_task_template_id_mock.assert_called_once_with(
            task_template_id=adhoc_template_id)

    def test_with_duplicate_orders_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
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
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        validate_task_template_id_mock.assert_called_once_with(
            task_template_id=adhoc_template_id
        )

    def test_with_invalid_user_id_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        user_role_ids = ['ROLE_1', 'ROLE_2']

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock, \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock, \
            is_valid_user_id_for_given_project_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        validate_task_template_id_mock(mocker)
        get_user_role_ids_mock = get_user_role_ids_mock(mocker)
        get_user_role_ids_mock.return_value = user_role_ids

        is_valid_user_id_for_given_project_mock = \
            is_valid_user_id_for_given_project_mock(mocker)

        get_user_permitted_stage_ids_mock(mocker)

        from ib_adhoc_tasks.adapters.iam_service import InvalidUserId
        is_valid_user_id_for_given_project_mock.side_effect = InvalidUserId

        # Assert
        with pytest.raises(InvalidUserId):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        is_valid_user_id_for_given_project_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )

    def test_with_invalid_user_for_project_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        user_role_ids = ['ROLE_1', 'ROLE_2']

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock, \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock, \
            is_valid_user_id_for_given_project_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        validate_task_template_id_mock(mocker)
        get_user_role_ids_mock = get_user_role_ids_mock(mocker)
        get_user_role_ids_mock.return_value = user_role_ids

        is_valid_user_id_for_given_project_mock = \
            is_valid_user_id_for_given_project_mock(mocker)

        get_user_permitted_stage_ids_mock(mocker)

        from ib_adhoc_tasks.adapters.iam_service import InvalidUserForProject
        is_valid_user_id_for_given_project_mock.side_effect = \
            InvalidUserForProject

        # Assert
        with pytest.raises(InvalidUserForProject):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        is_valid_user_id_for_given_project_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )

    def test_with_invalid_user_role_ids_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        user_role_ids = ['ROLE_1', 'ROLE_2']

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock, \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock, \
            is_valid_user_id_for_given_project_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids

        is_valid_user_id_for_given_project_mock = \
            is_valid_user_id_for_given_project_mock(mocker)
        is_valid_user_id_for_given_project_mock.return_value = True

        validate_task_template_id_mock(mocker)
        get_user_role_ids_mock = get_user_role_ids_mock(mocker)
        get_user_role_ids_mock.return_value = user_role_ids

        get_user_permitted_stage_ids_mock = get_user_permitted_stage_ids_mock(
            mocker)
        from ib_adhoc_tasks.adapters.task_service import \
            InvalidRoleIdsException
        get_user_permitted_stage_ids_mock.side_effect = InvalidRoleIdsException(
            role_ids=user_role_ids
        )

        # Assert
        with pytest.raises(InvalidRoleIdsException):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        get_user_permitted_stage_ids_mock.assert_called_once_with(
            user_role_ids=user_role_ids
        )

    def test_with_invalid_group_limit_value_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        for group_by_dto in group_by_dtos:
            group_by_dto.limit = -1

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidGroupLimitValue
        with pytest.raises(InvalidGroupLimitValue):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

    def test_with_invalid_group_offset_value_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        for group_by_dto in group_by_dtos:
            group_by_dto.offset = -1

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidGroupOffsetValue
        with pytest.raises(InvalidGroupOffsetValue):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

    def test_with_invalid_task_limit_value_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        task_offset_and_limit_values_dto.limit = -1

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidTaskLimitValue
        with pytest.raises(InvalidTaskLimitValue):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

    def test_with_invalid_task_offset_value_raise_exception(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        task_offset_and_limit_values_dto.offset = -1

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)

        # Assert
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidTaskOffsetValue
        with pytest.raises(InvalidTaskOffsetValue):
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

    def test_with_valid_details_return_response(
            self, interactor, elastic_storage, group_by_dtos, mocker,
            task_offset_and_limit_values_dto
    ):
        # Arrange
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        group_by_dtos = group_by_dtos
        valid_project_ids = ["PROJECT_1"]
        stage_ids = ['STAGE_1', 'STAGE_2']

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock, \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock, \
            is_valid_user_id_for_given_project_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)
        get_user_role_ids_mock(mocker)
        is_valid_user_id_for_given_project_mock = is_valid_user_id_for_given_project_mock(mocker)
        is_valid_user_id_for_given_project_mock.return_value = True

        get_user_permitted_stage_ids_mock = get_user_permitted_stage_ids_mock(
            mocker)
        get_user_permitted_stage_ids_mock.return_value = stage_ids

        expected_get_group_details_of_project_mock = Mock(), 0, 0
        elastic_storage.get_group_details_of_project.return_value = \
            expected_get_group_details_of_project_mock

        # Act
        response = interactor.get_task_ids_for_view(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos, user_id=user_id,
            task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
        )

        # Assert
        assert response == expected_get_group_details_of_project_mock
        elastic_storage.get_group_details_of_project.assert_called_once_with(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos, stage_ids=stage_ids,
            task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
        )
