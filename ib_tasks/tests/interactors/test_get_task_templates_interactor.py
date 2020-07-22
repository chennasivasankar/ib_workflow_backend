import pytest
import mock
from ib_tasks.interactors.get_task_templates_interactor \
    import GetTaskTemplatesInteractor
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, ActionsOfTemplateDTOFactory, \
    UserFieldPermissionDTOFactory, CompleteTaskTemplatesDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, FieldDTOFactory
from ib_tasks.interactors.storage_interfaces.dtos import \
    CompleteTaskTemplatesDTO


class TestGetTaskTemplatesInteractor:
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.presenter_interface \
            import GetTaskTemplatesPresenterInterface
        presenter = mock.create_autospec(GetTaskTemplatesPresenterInterface)
        return presenter

    @pytest.fixture
    def presenter_response_mock(self):
        presenter_response = {
            "task_templates": [
                {
                    "template_id": "string",
                    "template_name": "string",
                    "actions": [
                        {
                            "action_id": "string",
                            "action_name": "string",
                            "button_text": "string",
                            "button_color": "string"
                        }
                    ],
                    "group_of_fields": [
                        {
                            "gof_id": "string",
                            "gof_display_name": "string",
                            "max_columns": 1,
                            "order": 1,
                            "enable_multiple_gofs": True,
                            "fields": [
                                {
                                    "field_type": "PLAIN_TEXT",
                                    "field_id": "string",
                                    "display_name": "string",
                                    "is_field_required": True,
                                    "field_values": "string",
                                    "allowed_formats": "string",
                                    "validation_regex": "string",
                                    "error_msg": "string",
                                    "tooltip": "string",
                                    "help_text": "string",
                                    "placeholder_text": "string",
                                    "is_field_readable": True,
                                    "is_field_writable": True
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        return presenter_response

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        ActionsOfTemplateDTOFactory.reset_sequence()
        FieldDTOFactory.reset_sequence()
        GoFDTOFactory.reset_sequence()
        UserFieldPermissionDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        CompleteTaskTemplatesDTOFactory.reset_sequence()

    def test_when_complete_task_details_exists(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=2)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos
        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
        )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_task_templates_present_raises_exception(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock):
        # Arrange
        user_id = 1
        from ib_tasks.constants.exception_messages import \
            TASK_TEMPLATES_DOES_NOT_EXISTS
        expected_err_message = TASK_TEMPLATES_DOES_NOT_EXISTS
        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = []
        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos

        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskTemplatesDoesNotExists

        # Act
        with pytest.raises(TaskTemplatesDoesNotExists) as err:
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert err.value.args[0] == expected_err_message

    def test_when_no_actions_for_templates_returns_empty_list_of_actions_of_templates(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = []
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)

        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=2)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos

        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
        )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_gofs_for_templates_return_empty_gofs_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(size=2)
        gof_dtos = []
        field_dtos = FieldDTOFactory.create_batch(size=4)

        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=2)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos

        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
        )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_field_dtos_returns_empty_field_dtos_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = []
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = []

        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=2)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos

        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_user_field_permissions_returns_empty_user_field_permissions_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)

        user_field_permission_dtos = []
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos

        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_gofs_to_task_templates_exists_return_empty_gofs_to_task_templates(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker):
        # Arrange
        user_id = 1
        expected_gof_ids = []
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC']
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock
        )

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)

        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=2)
        gof_to_task_template_dtos = []

        task_storage_mock.get_task_template_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_user_actions_of_templates_dtos.return_value = \
            actions_of_template_dtos
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            return_value = gof_dtos
        task_storage_mock.get_gofs_to_task_templates_dtos.return_value = \
            gof_to_task_template_dtos

        task_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        task_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        #Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_storage_mock.get_task_template_dtos.assert_called_once()
        task_storage_mock.get_user_actions_of_templates_dtos.\
            assert_called_once_with(roles=expected_roles)
        task_storage_mock.get_gofs_of_task_templates_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_gofs_to_task_templates_dtos.assert_called_once()
        task_storage_mock.get_fields_of_gofs_in_dtos.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_storage_mock.get_user_field_permission_dtos.\
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )
