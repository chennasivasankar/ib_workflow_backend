import factory
import mock
import pytest

from ib_tasks.interactors.get_transition_template_interactor \
    import GetTransitionTemplateInteractor
from ib_tasks.interactors.presenter_interfaces. \
    get_transition_template_presenter_interface import \
    CompleteTransitionTemplateDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids
# TODO refactor TaskTemplateDTOFactory to TemplateDTOFactory
# TODO refactor GoFToTaskTemplateDTOFactory to GoFToTemplateDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, UserFieldPermissionDTOFactory, FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, FieldPermissionDTOFactory


class TestGetTransitionTemplateInteractor:
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        return mock.create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            get_transition_template_presenter_interface \
            import GetTransitionTemplatePresenterInterface
        presenter = \
            mock.create_autospec(GetTransitionTemplatePresenterInterface)
        return presenter

    @pytest.fixture
    def presenter_response_mock(self):
        presenter_response = {
            "transition_template_id": "string",
            "transition_template_name": "string",
            "group_of_fields": [
                {
                    "gof_id": "string",
                    "gof_display_name": "string",
                    "max_columns": 1,
                    "order": 1,
                    "enable_add_another": True,
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
                            "is_field_writable": True
                        }
                    ]
                }
            ]
        }
        return presenter_response

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        FieldDTOFactory.reset_sequence()
        GoFDTOFactory.reset_sequence()
        UserFieldPermissionDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.is_field_writable.reset()

    def test_when_complete_transition_template_details_exists(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        transition_template_id = "transition_template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                          'FIN_PAYMENT_POC',
                          'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                          'FIN_COMPLIANCE_APPROVER',
                          'FIN_PAYMENTS_LEVEL1_VERIFIER',
                          'FIN_PAYMENTS_LEVEL2_VERIFIER',
                          'FIN_PAYMENTS_LEVEL3_VERIFIER',
                          'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                          'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                          'FIN_ACCOUNTS_LEVEL2_VERIFIER']

        transition_template_dto = TaskTemplateDTOFactory.create()
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        task_template_storage_mock.check_is_transition_template_exists. \
            return_value = True
        task_template_storage_mock.get_transition_template_dto.return_value = \
            transition_template_dto
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_template_from_permitted_gofs. \
            return_value = gof_to_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_transition_template_response.return_value = \
            presenter_response_mock

        complete_transition_template_dto = CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gof_dtos,
            gofs_of_transition_template_dtos=gof_to_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        transition_template_interactor = GetTransitionTemplateInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_transition_template = \
            transition_template_interactor.get_transition_template_wrapper(
                user_id=user_id, presenter=presenter_mock,
                transition_template_id=transition_template_id
            )

        # Assert
        assert complete_transition_template == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.check_is_transition_template_exists. \
            assert_called_once_with(
                transition_template_id=transition_template_id
            )
        task_template_storage_mock. \
            get_transition_template_dto.assert_called_once()
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_template_from_permitted_gofs.assert_called_once_with(
                gof_ids=expected_gof_ids, template_id=transition_template_id
            )
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_transition_template_response. \
            assert_called_once_with(
                complete_transition_template_dto=
                complete_transition_template_dto
            )

    def test_with_invalid_transition_template_id_raises_exception(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        transition_template_id = "transition_template_1"
        task_template_storage_mock.check_is_transition_template_exists. \
            return_value = False

        from unittest.mock import Mock
        mock_object = Mock()
        presenter_mock.raise_transition_template_does_not_exists_exception. \
            return_value = mock_object
        transition_template_interactor = GetTransitionTemplateInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        response = \
            transition_template_interactor.get_transition_template_wrapper(
                user_id=user_id, presenter=presenter_mock,
                transition_template_id=transition_template_id
            )

        # Assert
        assert response == mock_object
        call_args = presenter_mock. \
            raise_transition_template_does_not_exists_exception.call_args
        assert call_args.args[0].args[0] == transition_template_id
        task_template_storage_mock.check_is_transition_template_exists. \
            assert_called_once_with(
                transition_template_id=transition_template_id
            )

    def test_when_no_gofs_exists_returns_empty_gofs_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        transition_template_id = "transition_template_1"
        expected_gof_ids = []
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                          'FIN_PAYMENT_POC',
                          'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                          'FIN_COMPLIANCE_APPROVER',
                          'FIN_PAYMENTS_LEVEL1_VERIFIER',
                          'FIN_PAYMENTS_LEVEL2_VERIFIER',
                          'FIN_PAYMENTS_LEVEL3_VERIFIER',
                          'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                          'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                          'FIN_ACCOUNTS_LEVEL2_VERIFIER']

        transition_template_dto = TaskTemplateDTOFactory.create()
        gof_dtos = []
        field_dtos = FieldDTOFactory.create_batch(size=4)
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        task_template_storage_mock.check_is_transition_template_exists. \
            return_value = True
        task_template_storage_mock.get_transition_template_dto.return_value = \
            transition_template_dto
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_template_from_permitted_gofs. \
            return_value = gof_to_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_transition_template_response.return_value = \
            presenter_response_mock

        complete_transition_template_dto = CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gof_dtos,
            gofs_of_transition_template_dtos=gof_to_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        transition_template_interactor = GetTransitionTemplateInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_transition_template = \
            transition_template_interactor.get_transition_template_wrapper(
                user_id=user_id, presenter=presenter_mock,
                transition_template_id=transition_template_id
            )

        # Assert
        assert complete_transition_template == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.check_is_transition_template_exists. \
            assert_called_once_with(
                transition_template_id=transition_template_id
            )
        task_template_storage_mock. \
            get_transition_template_dto.assert_called_once()
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_template_from_permitted_gofs.assert_called_once_with(
                gof_ids=expected_gof_ids, template_id=transition_template_id
            )
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_transition_template_response. \
            assert_called_once_with(
                complete_transition_template_dto=
                complete_transition_template_dto
            )

    def test_when_no_fields_exists_returns_empty_fields_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        transition_template_id = "transition_template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = []
        expected_roles = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                          'FIN_PAYMENT_POC',
                          'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                          'FIN_COMPLIANCE_APPROVER',
                          'FIN_PAYMENTS_LEVEL1_VERIFIER',
                          'FIN_PAYMENTS_LEVEL2_VERIFIER',
                          'FIN_PAYMENTS_LEVEL3_VERIFIER',
                          'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                          'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                          'FIN_ACCOUNTS_LEVEL2_VERIFIER']

        transition_template_dto = TaskTemplateDTOFactory.create()
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = []
        user_field_permission_dtos = []
        field_with_permissions_dtos = []
        gof_to_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        task_template_storage_mock.check_is_transition_template_exists. \
            return_value = True
        task_template_storage_mock.get_transition_template_dto.return_value = \
            transition_template_dto
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_template_from_permitted_gofs. \
            return_value = gof_to_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_transition_template_response.return_value = \
            presenter_response_mock

        complete_transition_template_dto = CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gof_dtos,
            gofs_of_transition_template_dtos=gof_to_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        transition_template_interactor = GetTransitionTemplateInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_transition_template = \
            transition_template_interactor.get_transition_template_wrapper(
                user_id=user_id, presenter=presenter_mock,
                transition_template_id=transition_template_id
            )

        # Assert
        assert complete_transition_template == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.check_is_transition_template_exists. \
            assert_called_once_with(
                transition_template_id=transition_template_id
            )
        task_template_storage_mock. \
            get_transition_template_dto.assert_called_once()
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_template_from_permitted_gofs.assert_called_once_with(
                gof_ids=expected_gof_ids, template_id=transition_template_id
            )
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_transition_template_response. \
            assert_called_once_with(
                complete_transition_template_dto=
                complete_transition_template_dto
            )

    def test_when_no_gofs_to_template_exists_returns_empty_gofs_to_template(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        transition_template_id = "transition_template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_roles = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                          'FIN_PAYMENT_POC',
                          'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                          'FIN_COMPLIANCE_APPROVER',
                          'FIN_PAYMENTS_LEVEL1_VERIFIER',
                          'FIN_PAYMENTS_LEVEL2_VERIFIER',
                          'FIN_PAYMENTS_LEVEL3_VERIFIER',
                          'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                          'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                          'FIN_ACCOUNTS_LEVEL2_VERIFIER']

        transition_template_dto = TaskTemplateDTOFactory.create()
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_template_dtos = []

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        task_template_storage_mock.check_is_transition_template_exists. \
            return_value = True
        task_template_storage_mock.get_transition_template_dto.return_value = \
            transition_template_dto
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_template_from_permitted_gofs. \
            return_value = gof_to_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        presenter_mock.get_transition_template_response.return_value = \
            presenter_response_mock

        complete_transition_template_dto = CompleteTransitionTemplateDTO(
            transition_template_dto=transition_template_dto,
            gof_dtos=gof_dtos,
            gofs_of_transition_template_dtos=gof_to_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        transition_template_interactor = GetTransitionTemplateInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_transition_template = \
            transition_template_interactor.get_transition_template_wrapper(
                user_id=user_id, presenter=presenter_mock,
                transition_template_id=transition_template_id
            )

        # Assert
        assert complete_transition_template == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.check_is_transition_template_exists. \
            assert_called_once_with(
                transition_template_id=transition_template_id
            )
        task_template_storage_mock. \
            get_transition_template_dto.assert_called_once()
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_template_from_permitted_gofs.assert_called_once_with(
                gof_ids=expected_gof_ids, template_id=transition_template_id
            )
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        presenter_mock.get_transition_template_response. \
            assert_called_once_with(
                complete_transition_template_dto=
                complete_transition_template_dto
            )
