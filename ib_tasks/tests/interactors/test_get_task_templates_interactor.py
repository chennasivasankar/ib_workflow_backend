from typing import List

import factory
import mock
import pytest

from ib_tasks.interactors.get_task_templates_interactor \
    import GetTaskTemplatesInteractor
from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import \
    CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    ActionWithStageIdDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    UserFieldPermissionDTO, FieldDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, \
    GoFToTaskTemplateDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO, ProjectIdWithTaskTemplateIdDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids
from ib_tasks.tests.common_fixtures.interactors import \
    get_gof_ids_having_read_permission_for_user_mock, \
    prepare_get_field_ids_having_write_permission_for_user
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, ActionWithStageIdDTOFactory, \
    UserFieldPermissionDTOFactory, FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, \
    FieldPermissionDTOFactory, StageIdWithTemplateIdDTOFactory, \
    ProjectIdWithTaskTemplateIdDTOFactory


class TestGetTaskTemplatesInteractor:
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
            get_task_templates_presenter_interface \
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
                            "action_id": 0,
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
        ActionWithStageIdDTOFactory.reset_sequence(1)
        FieldDTOFactory.reset_sequence()
        GoFDTOFactory.reset_sequence()
        UserFieldPermissionDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.is_field_writable.reset()
        StageIdWithTemplateIdDTOFactory.reset_sequence(1)
        ProjectIdWithTaskTemplateIdDTOFactory.reset_sequence(1)

    @pytest.fixture(autouse=True)
    def _prepare_storage_mock_methods_and_get_complete_task_templated_dto(
            self, task_template_storage_mock, task_storage_mock,
            field_storage_mock, presenter_mock, gof_storage_mock,
            presenter_response_mock, mocker
    ):
        gof_ids = ['gof_1', 'gof_2']
        field_ids = ['field0', 'field1', 'field2', 'field3']

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, gof_id=factory.Iterator(gof_ids))
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        self._prepare_task_template_storage_mock_method(
            task_template_storage_mock, task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            gof_to_task_template_dtos=gof_to_task_template_dtos)
        self._prepare_task_storage_mock_method(
            task_storage_mock,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos)
        self._prepare_gof_storage_mock_method(
            gof_storage_mock, gof_ids=gof_ids, gof_dtos=gof_dtos)
        self._prepare_field_storage_mock_method(
            field_storage_mock, field_ids=field_ids,
            user_field_permission_dtos=List[UserFieldPermissionDTO])

        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

    @staticmethod
    def _prepare_task_template_storage_mock_method(
            task_template_storage_mock, task_template_dtos: List[TemplateDTO],
            project_id_with_task_template_id_dtos:
            List[ProjectIdWithTaskTemplateIdDTO],
            gof_to_task_template_dtos: List[GoFToTaskTemplateDTO]):
        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos

    @staticmethod
    def _prepare_task_storage_mock_method(
            task_storage_mock,
            stage_id_with_template_id_dtos: List[StageIdWithTemplateIdDTO],
            action_with_stage_id_dtos: List[ActionWithStageIdDTO]):
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos

    @staticmethod
    def _prepare_gof_storage_mock_method(
            gof_storage_mock, gof_ids: List[str], gof_dtos: List[GoFDTO]):
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos

    @staticmethod
    def _prepare_field_storage_mock_method(
            field_storage_mock, field_ids: List[str],
            user_field_permission_dtos: List[UserFieldPermissionDTO],
            field_dtos: List[FieldDTO]):
        field_storage_mock.get_field_ids_for_given_gofs.return_value = \
            field_ids
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos

    def test_when_complete_task_details_exists(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = [1, 2]

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_task_templates_present_raises_exception(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        task_template_dtos = []

        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos

        from unittest.mock import Mock
        mock_object = Mock()
        presenter_mock.raise_task_templates_does_not_exists_exception. \
            return_value = mock_object
        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        response = task_template_interactor.get_task_templates_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        presenter_mock.raise_task_templates_does_not_exists_exception. \
            assert_called_once()

    def test_when_no_actions_for_templates_returns_empty_list_of_actions_of_templates(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = []

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = []
        action_with_stage_id_dtos = []
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, gof_id=factory.Iterator(expected_gof_ids))
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_gofs_for_templates_return_empty_gofs_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = []
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = [1, 2]

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
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
        gof_to_task_template_dtos = []
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_field_dtos_returns_empty_field_dtos_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = []
        expected_stage_ids = [1, 2]

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = []
        user_field_permission_dtos = []
        field_with_permissions_dtos = []
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=[])
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=[])
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_user_field_permissions_returns_empty_user_field_permissions_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        gof_ids = ['gof_1', 'gof_2']
        expected_gof_ids = []
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = [1, 2]

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, gof_id=factory.Iterator(gof_ids))
        user_field_permission_dtos = []
        field_with_permissions_dtos = []
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_gofs_to_task_templates_exists_return_empty_gofs_to_task_templates(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = [1, 2]

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, gof_id=factory.Iterator(expected_gof_ids))
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_task_template_dtos = []
        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )

    def test_when_no_project_task_templates_exists_returns_empty_list(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock
    ):
        # Arrange
        user_id = "user_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ['field0', 'field1', 'field2', 'field3']
        expected_stage_ids = [1, 2]

        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        expected_roles = get_user_role_ids_mock_method.return_value

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, gof_id=factory.Iterator(expected_gof_ids))
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(
                size=2, field_id=factory.Iterator(expected_field_ids)
            )
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        project_id_with_task_template_id_dtos = []

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            task_template_dtos
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = action_with_stage_id_dtos
        gof_storage_mock.get_gof_ids_with_read_permission_for_user \
            .return_value = expected_gof_ids
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = gof_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_permitted_gofs. \
            return_value = gof_to_task_template_dtos
        field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
        field_storage_mock.get_user_field_permission_dtos.return_value = \
            user_field_permission_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = project_id_with_task_template_id_dtos
        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock
        get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        task_template_storage_mock \
            .get_gofs_to_templates_from_permitted_gofs. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
            assert_called_once_with(user_roles=expected_roles)
        field_storage_mock.get_fields_of_gofs_in_dtos. \
            assert_called_once_with(gof_ids=expected_gof_ids)
        field_storage_mock.get_user_field_permission_dtos. \
            assert_called_once_with(
                roles=expected_roles, field_ids=expected_field_ids
            )
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_templates_dto
        )
