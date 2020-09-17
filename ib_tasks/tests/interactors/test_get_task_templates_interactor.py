from typing import List

import mock
import pytest

from ib_tasks.interactors.get_task_templates_interactor \
    import GetTaskTemplatesInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldPermissionDTO
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    StageIdWithTemplateIdDTO, StageGoFWithTemplateIdDTO
from ib_tasks.interactors.storage_interfaces.task_templates_dtos import \
    TemplateDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids
from ib_tasks.tests.common_fixtures.interactors import \
    get_gof_ids_having_read_permission_for_user_mock, \
    get_field_ids_having_read_permission_for_user_mock, \
    prepare_get_field_ids_having_write_permission_for_user, \
    get_user_permitted_stage_ids_in_given_stage_ids_mock
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, ActionWithStageIdDTOFactory, \
    FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, \
    FieldPermissionDTOFactory, StageIdWithTemplateIdDTOFactory, \
    ProjectIdWithTaskTemplateIdDTOFactory, StageGoFWithTemplateIdDTOFactory


class TestGetTaskTemplatesInteractor:
    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        ActionWithStageIdDTOFactory.reset_sequence(1)
        FieldDTOFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFToTaskTemplateDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.is_field_writable.reset()
        StageIdWithTemplateIdDTOFactory.reset_sequence(1)
        ProjectIdWithTaskTemplateIdDTOFactory.reset_sequence(1)
        StageGoFWithTemplateIdDTOFactory.reset_sequence(1)

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
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        return mock.create_autospec(StageStorageInterface)

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

    @pytest.fixture
    def complete_task_template_dto(self):
        task_template_ids = ["template_1", "template_2"]
        gof_ids = ['gof_1', 'gof_2']
        stage_ids = [1, 2]

        import factory
        task_template_dtos = TaskTemplateDTOFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(
                size=2, stage_id=factory.Iterator(stage_ids))
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)

        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids))
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True]))
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        project_id_with_task_template_id_dtos = \
            ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
        stage_gof_with_template_id_dtos = \
            StageGoFWithTemplateIdDTOFactory.create_batch(
                size=2, stage_id=factory.Iterator(stage_ids),
                gof_id=factory.Iterator(gof_ids),
                task_template_id=factory.Iterator(task_template_ids))

        from ib_tasks.interactors.presenter_interfaces. \
            get_task_templates_presenter_interface import \
            CompleteTaskTemplatesDTO

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            project_id_with_task_template_id_dtos=
            project_id_with_task_template_id_dtos,
            initial_stage_id_with_template_id_dtos=
            stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos,
            stage_gof_with_template_id_dtos=stage_gof_with_template_id_dtos
        )
        return complete_task_templates_dto

    @pytest.fixture
    def stage_id_with_template_id_dtos(self):
        from ib_tasks.tests.factories.storage_dtos import \
            StageIdWithTemplateIdDTOFactory
        StageIdWithTemplateIdDTOFactory.reset_sequence(1)

        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        return stage_id_with_template_id_dtos

    @pytest.fixture
    def stage_id_with_gof_id_dtos(self):
        from ib_tasks.tests.factories.storage_dtos import \
            StageIdWithGoFIdDTOFactory
        StageIdWithGoFIdDTOFactory.reset_sequence(1)

        stage_id_with_gof_id_dtos = StageIdWithGoFIdDTOFactory.create_batch(
            size=2
        )
        return stage_id_with_gof_id_dtos

    @staticmethod
    def _get_field_ids(field_dtos: List[FieldDTO]) -> List[str]:
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        return field_ids

    @staticmethod
    def _get_field_dtos(field_permission_dtos: List[FieldPermissionDTO]
                       ) -> List[FieldDTO]:
        field_dtos = [
            field_permission_dto.field_dto
            for field_permission_dto in field_permission_dtos
        ]
        return field_dtos

    @staticmethod
    def _get_gof_ids(gof_dtos: List[GoFDTO]) -> List[str]:
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        return gof_ids

    @staticmethod
    def _get_task_template_ids(
            task_template_dtos: List[TemplateDTO]) -> List[str]:
        task_template_ids = [
            task_template_dto.template_id
            for task_template_dto in task_template_dtos
        ]
        return task_template_ids

    @staticmethod
    def _get_initial_stage_ids(
            initial_stage_id_with_template_id_dtos:
            List[StageIdWithTemplateIdDTO]) -> List[int]:
        initial_stage_ids = [
            initial_stage_id_with_template_id_dto.stage_id
            for initial_stage_id_with_template_id_dto in
            initial_stage_id_with_template_id_dtos
        ]
        return initial_stage_ids

    @staticmethod
    def _get_field_ids_having_writable_permission(
            field_permissions_dtos: List[FieldPermissionDTO]) -> List[str]:
        field_ids_having_writable_permission = [
            field_permissions_dto.field_dto.field_id
            for field_permissions_dto in field_permissions_dtos
            if field_permissions_dto.is_field_writable
        ]
        return field_ids_having_writable_permission

    @staticmethod
    def _get_stage_ids(
            stage_gof_with_template_id_dtos: List[StageGoFWithTemplateIdDTO]
    ) -> List[int]:
        stage_ids = [
            stage_gof_with_template_id_dto.stage_id
            for stage_gof_with_template_id_dto in
            stage_gof_with_template_id_dtos
        ]
        return stage_ids

    def _check_storage_and_presenter_mock_calls(
            self, task_storage_mock, presenter_mock, stage_storage_mock,
            presenter_response_mock,
            field_storage_mock, gof_storage_mock, task_template_storage_mock,
            complete_task_template_dto, stage_id_with_template_id_dtos,
            stage_id_with_gof_id_dtos
    ):
        field_permissions_dtos = \
            complete_task_template_dto.field_with_permissions_dtos
        field_dtos = self._get_field_dtos(
            field_permission_dtos=field_permissions_dtos)
        field_ids = self._get_field_ids(field_dtos=field_dtos)
        gof_dtos = complete_task_template_dto.gof_dtos
        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        task_template_ids = self._get_task_template_ids(
            task_template_dtos=complete_task_template_dto.task_template_dtos)
        initial_stage_ids = self._get_initial_stage_ids(
            initial_stage_id_with_template_id_dtos=
            complete_task_template_dto.initial_stage_id_with_template_id_dtos)
        stage_ids = self._get_stage_ids(
            stage_gof_with_template_id_dtos=
            complete_task_template_dto.stage_gof_with_template_id_dtos
        )

        task_template_storage_mock.get_task_templates_dtos.assert_called_once()
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            assert_called_once()
        task_template_storage_mock.get_gofs_to_templates_from_given_gofs. \
            assert_called_once_with(gof_ids=gof_ids)
        task_template_storage_mock.get_gof_ids_of_templates.\
            assert_called_once_with(template_ids=task_template_ids)

        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            assert_called_once()
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            assert_called_once_with(stage_ids=initial_stage_ids)

        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            assert_called_once_with(gof_ids=gof_ids)

        field_storage_mock.get_field_ids_for_given_gofs.\
            assert_called_once_with(gof_ids=gof_ids)
        field_storage_mock.get_field_dtos.assert_called_once_with(
            field_ids=field_ids)

        stage_storage_mock.get_stage_id_with_template_id_dtos.\
            assert_called_once_with(task_template_ids=task_template_ids)
        stage_storage_mock.get_stage_gof_dtos_for_given_stages_and_gofs. \
            assert_called_once_with(stage_ids=stage_ids, gof_ids=gof_ids)
        presenter_mock.get_task_templates_response.assert_called_once_with(
            complete_task_templates_dto=complete_task_template_dto
        )

    def _make_storage_and_presenter_mocks(
            self, task_storage_mock, presenter_mock, stage_storage_mock,
            presenter_response_mock,
            field_storage_mock, gof_storage_mock, task_template_storage_mock,
            complete_task_template_dto, stage_id_with_template_id_dtos,
            stage_id_with_gof_id_dtos
    ):
        gof_dtos = complete_task_template_dto.gof_dtos
        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        field_permissions_dtos = \
            complete_task_template_dto.field_with_permissions_dtos
        field_dtos = self._get_field_dtos(
            field_permission_dtos=field_permissions_dtos)
        field_ids = self._get_field_ids(field_dtos=field_dtos)

        task_template_storage_mock.get_task_templates_dtos.return_value = \
            complete_task_template_dto.task_template_dtos
        task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
            return_value = \
            complete_task_template_dto.project_id_with_task_template_id_dtos
        task_template_storage_mock. \
            get_gofs_to_templates_from_given_gofs.return_value = \
            complete_task_template_dto.gofs_of_task_templates_dtos
        task_template_storage_mock.get_gof_ids_of_templates.return_value = \
            gof_ids

        task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
            return_value = \
            complete_task_template_dto.initial_stage_id_with_template_id_dtos
        task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
            return_value = \
            complete_task_template_dto.action_with_stage_id_dtos

        gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
            return_value = complete_task_template_dto.gof_dtos

        field_storage_mock.get_field_ids_for_given_gofs.return_value = \
            field_ids
        field_storage_mock.get_field_dtos.return_value = field_dtos

        stage_storage_mock.get_stage_id_with_template_id_dtos.return_value = \
            stage_id_with_template_id_dtos
        stage_storage_mock.get_stage_gof_dtos_for_given_stages_and_gofs. \
            return_value = stage_id_with_gof_id_dtos

    def test_when_complete_task_details_exists(
            self, task_storage_mock, presenter_mock, stage_storage_mock,
            presenter_response_mock, mocker,
            field_storage_mock, gof_storage_mock, task_template_storage_mock,
            complete_task_template_dto, stage_id_with_template_id_dtos,
            stage_id_with_gof_id_dtos
    ):
        # Arrange
        user_id = "user_1"

        gof_dtos = complete_task_template_dto.gof_dtos
        gof_ids = self._get_gof_ids(gof_dtos=gof_dtos)
        field_permissions_dtos = \
            complete_task_template_dto.field_with_permissions_dtos
        field_dtos = self._get_field_dtos(
            field_permission_dtos=field_permissions_dtos)
        field_ids = self._get_field_ids(field_dtos=field_dtos)
        stage_ids = self._get_stage_ids(
            stage_gof_with_template_id_dtos=
            complete_task_template_dto.stage_gof_with_template_id_dtos
        )
        field_ids_having_writable_permission = \
            self._get_field_ids_having_writable_permission(
                field_permissions_dtos=field_permissions_dtos)

        self._make_storage_and_presenter_mocks(
            task_storage_mock, presenter_mock, stage_storage_mock,
            presenter_response_mock,
            field_storage_mock, gof_storage_mock, task_template_storage_mock,
            complete_task_template_dto, stage_id_with_template_id_dtos,
            stage_id_with_gof_id_dtos
        )

        get_user_role_ids_mock_object = get_user_role_ids(mocker)
        user_roles = get_user_role_ids_mock_object.return_value

        get_field_ids_having_read_permission_for_user_mock_object = \
            get_field_ids_having_read_permission_for_user_mock(mocker)
        get_field_ids_having_read_permission_for_user_mock_object.\
            return_value = field_ids
        get_gof_ids_having_read_permission_for_user_mock_object = \
            get_gof_ids_having_read_permission_for_user_mock(mocker)
        prepare_get_field_ids_having_write_permission_for_user_mock_object = \
            prepare_get_field_ids_having_write_permission_for_user(
                mocker, field_ids_having_writable_permission)
        get_user_permitted_stage_ids_in_given_stage_ids_mock_object = \
            get_user_permitted_stage_ids_in_given_stage_ids_mock(
                mocker, stage_ids)

        presenter_mock.get_task_templates_response.return_value = \
            presenter_response_mock

        task_template_interactor = GetTaskTemplatesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock, field_storage=field_storage_mock,
        )

        # Act
        complete_task_templates = \
            task_template_interactor.get_task_templates_wrapper(
                user_id=user_id, presenter=presenter_mock
            )

        # Assert
        assert complete_task_templates == presenter_response_mock

        get_user_role_ids_mock_object.assert_called_once_with(user_id=user_id)
        get_field_ids_having_read_permission_for_user_mock_object.\
            assert_called_once_with(
                user_roles=user_roles, field_storage=field_storage_mock,
                field_ids=field_ids)
        get_gof_ids_having_read_permission_for_user_mock_object.\
            assert_called_once_with(
                user_roles=user_roles, gof_storage=gof_storage_mock,
                gof_ids=gof_ids)
        prepare_get_field_ids_having_write_permission_for_user_mock_object.\
            assert_called_once_with(
                user_roles=user_roles, field_storage=field_storage_mock,
                field_ids=field_ids)
        get_user_permitted_stage_ids_in_given_stage_ids_mock_object. \
            assert_called_once_with(
                user_roles=user_roles, stage_ids=stage_ids,
                stage_storage=stage_storage_mock)

        self._check_storage_and_presenter_mock_calls(
            task_storage_mock, presenter_mock, stage_storage_mock,
            presenter_response_mock, field_storage_mock, gof_storage_mock,
            task_template_storage_mock, complete_task_template_dto,
            stage_id_with_template_id_dtos, stage_id_with_gof_id_dtos)

    def test_when_no_task_templates_present_raises_exception(
            self, task_storage_mock, presenter_mock,
            presenter_response_mock, mocker, stage_storage_mock,
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
            gof_storage=gof_storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock
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

    # def test_when_no_actions_for_templates_returns_empty_list_of_actions_of_templates(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     expected_gof_ids = ['gof_1', 'gof_2']
    #     expected_field_ids = ['field0', 'field1', 'field2', 'field3']
    #     expected_stage_ids = []
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = []
    #     action_with_stage_id_dtos = []
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = FieldDTOFactory.create_batch(
    #         size=4, gof_id=factory.Iterator(expected_gof_ids))
    #     user_field_permission_dtos = \
    #         UserFieldPermissionDTOFactory.create_batch(
    #             size=2, field_id=factory.Iterator(expected_field_ids)
    #         )
    #     field_with_permissions_dtos = \
    #         FieldPermissionDTOFactory.create_batch(
    #             size=2, field_dto=factory.Iterator(field_dtos),
    #             is_field_writable=factory.Iterator([False, True])
    #         )
    #     gof_to_task_template_dtos = \
    #         GoFToTaskTemplateDTOFactory.create_batch(size=2)
    #     project_id_with_task_template_id_dtos = \
    #         ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
    #
    # def test_when_no_gofs_for_templates_return_empty_gofs_list(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     expected_gof_ids = []
    #     expected_field_ids = ['field0', 'field1', 'field2', 'field3']
    #     expected_stage_ids = [1, 2]
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = \
    #         StageIdWithTemplateIdDTOFactory.create_batch(size=2)
    #     action_with_stage_id_dtos = \
    #         ActionWithStageIdDTOFactory.create_batch(size=2)
    #     gof_dtos = []
    #     field_dtos = FieldDTOFactory.create_batch(size=4)
    #     user_field_permission_dtos = \
    #         UserFieldPermissionDTOFactory.create_batch(
    #             size=2, field_id=factory.Iterator(expected_field_ids)
    #         )
    #     field_with_permissions_dtos = \
    #         FieldPermissionDTOFactory.create_batch(
    #             size=2, field_dto=factory.Iterator(field_dtos),
    #             is_field_writable=factory.Iterator([False, True])
    #         )
    #     gof_to_task_template_dtos = []
    #     project_id_with_task_template_id_dtos = \
    #         ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
    #
    # def test_when_no_field_dtos_returns_empty_field_dtos_list(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     expected_gof_ids = ['gof_1', 'gof_2']
    #     expected_field_ids = []
    #     expected_stage_ids = [1, 2]
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = \
    #         StageIdWithTemplateIdDTOFactory.create_batch(size=2)
    #     action_with_stage_id_dtos = \
    #         ActionWithStageIdDTOFactory.create_batch(size=2)
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = []
    #     user_field_permission_dtos = []
    #     field_with_permissions_dtos = []
    #     gof_to_task_template_dtos = \
    #         GoFToTaskTemplateDTOFactory.create_batch(size=2)
    #     project_id_with_task_template_id_dtos = \
    #         ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=[])
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=[])
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
    #
    # def test_when_no_user_field_permissions_returns_empty_user_field_permissions_list(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     gof_ids = ['gof_1', 'gof_2']
    #     expected_gof_ids = []
    #     expected_field_ids = ['field0', 'field1', 'field2', 'field3']
    #     expected_stage_ids = [1, 2]
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = \
    #         StageIdWithTemplateIdDTOFactory.create_batch(size=2)
    #     action_with_stage_id_dtos = \
    #         ActionWithStageIdDTOFactory.create_batch(size=2)
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = FieldDTOFactory.create_batch(
    #         size=4, gof_id=factory.Iterator(gof_ids))
    #     user_field_permission_dtos = []
    #     field_with_permissions_dtos = []
    #     gof_to_task_template_dtos = \
    #         GoFToTaskTemplateDTOFactory.create_batch(size=2)
    #     project_id_with_task_template_id_dtos = \
    #         ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
    #
    # def test_when_no_gofs_to_task_templates_exists_return_empty_gofs_to_task_templates(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     expected_gof_ids = ['gof_1', 'gof_2']
    #     expected_field_ids = ['field0', 'field1', 'field2', 'field3']
    #     expected_stage_ids = [1, 2]
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = \
    #         StageIdWithTemplateIdDTOFactory.create_batch(size=2)
    #     action_with_stage_id_dtos = \
    #         ActionWithStageIdDTOFactory.create_batch(size=2)
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = FieldDTOFactory.create_batch(
    #         size=4, gof_id=factory.Iterator(expected_gof_ids))
    #     user_field_permission_dtos = \
    #         UserFieldPermissionDTOFactory.create_batch(
    #             size=2, field_id=factory.Iterator(expected_field_ids)
    #         )
    #     field_with_permissions_dtos = \
    #         FieldPermissionDTOFactory.create_batch(
    #             size=2, field_dto=factory.Iterator(field_dtos),
    #             is_field_writable=factory.Iterator([False, True])
    #         )
    #     gof_to_task_template_dtos = []
    #     project_id_with_task_template_id_dtos = \
    #         ProjectIdWithTaskTemplateIdDTOFactory.create_batch(size=2)
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
    #
    # def test_when_no_project_task_templates_exists_returns_empty_list(
    #         self, task_storage_mock, presenter_mock,
    #         presenter_response_mock, mocker,
    #         field_storage_mock, gof_storage_mock, task_template_storage_mock
    # ):
    #     # Arrange
    #     user_id = "user_1"
    #     expected_gof_ids = ['gof_1', 'gof_2']
    #     expected_field_ids = ['field0', 'field1', 'field2', 'field3']
    #     expected_stage_ids = [1, 2]
    #
    #     get_user_role_ids_mock_method = get_user_role_ids(mocker)
    #     expected_roles = get_user_role_ids_mock_method.return_value
    #
    #     task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
    #     stage_id_with_template_id_dtos = \
    #         StageIdWithTemplateIdDTOFactory.create_batch(size=2)
    #     action_with_stage_id_dtos = \
    #         ActionWithStageIdDTOFactory.create_batch(size=2)
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = FieldDTOFactory.create_batch(
    #         size=4, gof_id=factory.Iterator(expected_gof_ids))
    #     user_field_permission_dtos = \
    #         UserFieldPermissionDTOFactory.create_batch(
    #             size=2, field_id=factory.Iterator(expected_field_ids)
    #         )
    #     field_with_permissions_dtos = \
    #         FieldPermissionDTOFactory.create_batch(
    #             size=2, field_dto=factory.Iterator(field_dtos),
    #             is_field_writable=factory.Iterator([False, True])
    #         )
    #     gof_to_task_template_dtos = \
    #         GoFToTaskTemplateDTOFactory.create_batch(size=2)
    #     project_id_with_task_template_id_dtos = []
    #
    #     task_template_storage_mock.get_task_templates_dtos.return_value = \
    #         task_template_dtos
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         return_value = stage_id_with_template_id_dtos
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         return_value = action_with_stage_id_dtos
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user \
    #         .return_value = expected_gof_ids
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         return_value = gof_dtos
    #     task_template_storage_mock. \
    #         get_gofs_to_templates_from_permitted_gofs. \
    #         return_value = gof_to_task_template_dtos
    #     field_storage_mock.get_fields_of_gofs_in_dtos.return_value = field_dtos
    #     field_storage_mock.get_user_field_permission_dtos.return_value = \
    #         user_field_permission_dtos
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         return_value = project_id_with_task_template_id_dtos
    #     presenter_mock.get_task_templates_response.return_value = \
    #         presenter_response_mock
    #
    #     complete_task_templates_dto = CompleteTaskTemplatesDTO(
    #         task_template_dtos=task_template_dtos,
    #         project_id_with_task_template_id_dtos=
    #         project_id_with_task_template_id_dtos,
    #         stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
    #         action_with_stage_id_dtos=action_with_stage_id_dtos,
    #         gof_dtos=gof_dtos,
    #         gofs_of_task_templates_dtos=gof_to_task_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     task_template_interactor = GetTaskTemplatesInteractor(
    #         task_storage=task_storage_mock,
    #         task_template_storage=task_template_storage_mock,
    #         gof_storage=gof_storage_mock, field_storage=field_storage_mock
    #     )
    #
    #     # Act
    #     complete_task_templates = \
    #         task_template_interactor.get_task_templates_wrapper(
    #             user_id=user_id, presenter=presenter_mock
    #         )
    #
    #     # Assert
    #     assert complete_task_templates == presenter_response_mock
    #     get_user_role_ids_mock_method.assert_called_once_with(user_id=user_id)
    #     task_template_storage_mock.get_task_templates_dtos.assert_called_once()
    #     task_storage_mock.get_initial_stage_id_with_template_id_dtos. \
    #         assert_called_once()
    #     task_storage_mock.get_actions_for_given_stage_ids_in_dtos. \
    #         assert_called_once_with(stage_ids=expected_stage_ids)
    #     gof_storage_mock.get_gofs_details_dtos_for_given_gof_ids. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     task_template_storage_mock \
    #         .get_gofs_to_templates_from_permitted_gofs. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     gof_storage_mock.get_gof_ids_with_read_permission_for_user. \
    #         assert_called_once_with(user_roles=expected_roles)
    #     field_storage_mock.get_fields_of_gofs_in_dtos. \
    #         assert_called_once_with(gof_ids=expected_gof_ids)
    #     field_storage_mock.get_user_field_permission_dtos. \
    #         assert_called_once_with(
    #             roles=expected_roles, field_ids=expected_field_ids
    #         )
    #     task_template_storage_mock.get_project_id_with_task_template_id_dtos. \
    #         assert_called_once()
    #     presenter_mock.get_task_templates_response.assert_called_once_with(
    #         complete_task_templates_dto=complete_task_templates_dto
    #     )
