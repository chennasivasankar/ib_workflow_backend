import mock
import pytest


class TestGetTaskIdsForGroupInteractor:

    @pytest.fixture
    def elastic_storage_mock(self):
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticStorageInterface
        return mock.create_autospec(ElasticStorageInterface)

    @pytest.fixture
    def interactor(self, elastic_storage_mock):
        from ib_adhoc_tasks.interactors.get_task_ids_for_group_interactor import \
            GetTaskIdsForGroupInteractor
        return GetTaskIdsForGroupInteractor(
            elastic_storage=elastic_storage_mock
        )

    def test_given_invalid_project_id_raises_invalid_project_id_exception(
            self, interactor, elastic_storage_mock, mocker
    ):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            TaskIdsForGroupsParameterDTOFactory
        task_ids_for_groups_parameter_dto = TaskIdsForGroupsParameterDTOFactory()
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker=mocker)
        get_valid_project_ids_mock.return_value = []
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId

        with pytest.raises(InvalidProjectId):
            interactor.get_task_ids_for_groups(
                task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto
            )

        get_valid_project_ids_mock.assert_called_once_with(
            project_ids=[task_ids_for_groups_parameter_dto.project_id]
        )

    def test_given_invalid_template_id_raises_invalid_template_id_exception(
            self, interactor, elastic_storage_mock, mocker
    ):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            TaskIdsForGroupsParameterDTOFactory
        task_ids_for_groups_parameter_dto = TaskIdsForGroupsParameterDTOFactory()
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock, validate_task_template_id_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker=mocker)
        get_valid_project_ids_mock.return_value = \
            [task_ids_for_groups_parameter_dto.project_id]
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidTaskTemplateId
        validate_task_template_id_mock = validate_task_template_id_mock(
            mocker=mocker)
        validate_task_template_id_mock.side_effect = InvalidTaskTemplateId

        with pytest.raises(InvalidTaskTemplateId):
            interactor.get_task_ids_for_groups(
                task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto
            )

        validate_task_template_id_mock.assert_called_once_with(
            task_template_id=task_ids_for_groups_parameter_dto.template_id
        )

    def test_given_valid_data_it_returns_task_ids(
            self, interactor, elastic_storage_mock, mocker
    ):
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            TaskIdsForGroupsParameterDTOFactory
        task_ids_for_groups_parameter_dto = TaskIdsForGroupsParameterDTOFactory()
        user_role_ids = ["role_1", "role_2"]
        stage_ids = ["stage_id_1", "stage_id_2"]
        task_ids = ["task_id_1", "task_id_2"]
        from ib_adhoc_tasks.interactors.dtos.dtos import TaskIdsAndCountDTO
        expected_task_ids_and_count_dto = TaskIdsAndCountDTO(
            task_ids=task_ids, total_tasks_count=2
        )
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock = get_valid_project_ids_mock(mocker=mocker)
        get_valid_project_ids_mock.return_value = \
            [task_ids_for_groups_parameter_dto.project_id]
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock = \
            get_user_role_ids_based_on_project_mock(mocker=mocker)
        get_user_role_ids_based_on_project_mock.return_value = user_role_ids
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            get_user_permitted_stage_ids_mock
        get_stage_ids_based_on_user_roles_mock = \
            get_user_permitted_stage_ids_mock(mocker=mocker)
        get_stage_ids_based_on_user_roles_mock.return_value = stage_ids
        elastic_storage_mock. \
            get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail. \
            return_value = expected_task_ids_and_count_dto
        from ib_adhoc_tasks.tests.common_fixtures.adapters import \
            validate_task_template_id_mock
        validate_task_template_id_mock(mocker)

        actual_task_ids_and_count_dto = interactor.get_task_ids_for_groups(
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto
        )

        get_user_role_ids_based_on_project_mock.assert_called_once_with(
            user_id=task_ids_for_groups_parameter_dto.user_id,
            project_id=task_ids_for_groups_parameter_dto.project_id
        )
        get_stage_ids_based_on_user_roles_mock.assert_called_once_with(
            user_role_ids=user_role_ids
        )
        elastic_storage_mock. \
            get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto,
            stage_ids=stage_ids
        )
        assert actual_task_ids_and_count_dto == expected_task_ids_and_count_dto
