from unittest.mock import create_autospec

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
            self, interactor, elastic_storage, mocker,
            prepare_group_details_dtos,
            task_offset_and_limit_values_dto, prepare_group_count_dto,
            prepare_child_group_count_dtos,
            stage_id_and_name_dtos, snapshot
    ):
        # Arrange
        user_id = "USER_1"
        project_id = "PROJECT_1"
        adhoc_template_id = "ADHOC_TEMPLATE_ID"
        valid_project_ids = ["PROJECT_1"]
        stage_ids = ['STAGE_1', 'STAGE_2']
        total_groups_count = 5

        from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO
        group_by_dtos = [
            GroupByDTO(group_by_value="FIN_PURPOSE_OF_THE_ORDER", order=1,
                       offset=0, limit=5),
            GroupByDTO(group_by_value="STAGE", order=2, offset=0, limit=5)
        ]

        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock, \
            get_user_permitted_stage_ids_mock, get_user_role_ids_mock, \
            is_valid_user_id_for_given_project_mock, get_stage_details_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker)
        get_valid_project_ids_mock.return_value = valid_project_ids
        validate_task_template_id_mock(mocker)
        get_user_role_ids_mock(mocker)
        is_valid_user_id_for_given_project_mock = is_valid_user_id_for_given_project_mock(
            mocker)
        is_valid_user_id_for_given_project_mock.return_value = True

        get_user_permitted_stage_ids_mock = get_user_permitted_stage_ids_mock(
            mocker)
        get_user_permitted_stage_ids_mock.return_value = stage_ids

        get_stage_details_mock = get_stage_details_mock(mocker)
        get_stage_details_mock.return_value = stage_id_and_name_dtos

        expected_get_group_details_of_project_mock = \
            prepare_group_details_dtos, total_groups_count, prepare_child_group_count_dtos
        elastic_storage.get_group_details_of_project.return_value = \
            expected_get_group_details_of_project_mock

        # Act
        group_details_dtos, total_groups_count, child_group_count_dtos = \
            interactor.get_task_ids_for_view(
                project_id=project_id, adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos, user_id=user_id,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )

        # Assert
        elastic_storage.get_group_details_of_project.assert_called_once_with(
            project_id=project_id, adhoc_template_id=adhoc_template_id,
            group_by_dtos=group_by_dtos, stage_ids=stage_ids,
            task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
        )
        snapshot.assert_match(group_details_dtos, "group_details_dtos")
        snapshot.assert_match(total_groups_count, "total_groups_count")
        snapshot.assert_match(child_group_count_dtos, "child_group_count_dtos")

    @pytest.fixture()
    def prepare_group_details_dtos(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
            GroupDetailsDTO
        group_details_dtos = [
            GroupDetailsDTO(task_ids=[19], total_tasks=1,
                            group_by_value='need to pay debt',
                            group_by_display_name='need to pay debt',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[20], total_tasks=1,
                            group_by_value='need to pay friend',
                            group_by_display_name='need to pay friend',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[24], total_tasks=1,
                            group_by_value='purpose',
                            group_by_display_name='purpose',
                            child_group_by_value='PR_NEED_CLARIFICATION',
                            child_group_by_display_name='PR_NEED_CLARIFICATION'),
            GroupDetailsDTO(task_ids=[21], total_tasks=1,
                            group_by_value='sfsdd',
                            group_by_display_name='sfsdd',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS'),
            GroupDetailsDTO(task_ids=[25], total_tasks=1,
                            group_by_value='sfsdfsd',
                            group_by_display_name='sfsdfsd',
                            child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                            child_group_by_display_name='PR_PAYMENT_REQUEST_DRAFTS')]
        return group_details_dtos

    @pytest.fixture()
    def prepare_group_count_dto(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
            GroupCountDTO
        return GroupCountDTO(
            group_by_value='FIN_PURPOSE_OF_THE_ORDER', total_groups=5
        )

    @pytest.fixture()
    def prepare_child_group_count_dtos(self):
        from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
            ChildGroupCountDTO
        child_group_count_dtos = [
            ChildGroupCountDTO(group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                               total_child_groups=1),
            ChildGroupCountDTO(group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                               total_child_groups=1),
            ChildGroupCountDTO(group_by_value='PR_NEED_CLARIFICATION',
                               total_child_groups=1),
            ChildGroupCountDTO(group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                               total_child_groups=1),
            ChildGroupCountDTO(group_by_value='PR_PAYMENT_REQUEST_DRAFTS',
                               total_child_groups=1)]
        return child_group_count_dtos

    @pytest.fixture()
    def stage_id_and_name_dtos(self):
        from ib_adhoc_tasks.adapters.task_service import StageDisplayNameValueDTO
        stage_id_and_name_dtos = [
            StageDisplayNameValueDTO(stage_id='PR_NEED_CLARIFICATION',
                                     name='Need Clarification'),
            StageDisplayNameValueDTO(stage_id='PR_PAYMENT_REQUEST_DRAFTS',
                                     name='Payment Request Drafts')]
        return stage_id_and_name_dtos
