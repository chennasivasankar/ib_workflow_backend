import pytest

from ib_tasks.tests.factories.storage_dtos import ProjectTemplateDTOFactory, \
    TaskTemplateGofsDTOFactory, FieldNameDTOFactory
from ib_tasks.tests.factories.storage_dtos import TaskTemplateDTOFactory, \
    StageIdWithTemplateIdDTOFactory, \
    ActionWithStageIdDTOFactory, GoFDTOFactory, FieldDTOFactory, \
    FieldPermissionDTOFactory, GoFToTaskTemplateDTOFactory


class TestGetTaskTemplatesFieldsInteractor:

    @staticmethod
    @pytest.fixture()
    def interactor():
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
            GoFStorageInterface
        from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
            import TaskTemplateStorageInterface
        from unittest.mock import create_autospec
        field_storage = create_autospec(FieldsStorageInterface)
        gof_storage = create_autospec(GoFStorageInterface)
        task_template_storage = create_autospec(TaskTemplateStorageInterface)
        from ib_tasks.interactors.get_task_templates_fields_interactor \
            import GetTaskTemplatesFieldsInteractor
        interactor = GetTaskTemplatesFieldsInteractor(
            field_storage=field_storage,
            gof_storage=gof_storage,
            task_template_storage=task_template_storage
        )
        return interactor

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        ActionWithStageIdDTOFactory.reset_sequence()
        FieldDTOFactory.reset_sequence()
        GoFDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.is_field_writable.reset()
        StageIdWithTemplateIdDTOFactory.reset_sequence(1)

    @staticmethod
    @pytest.fixture()
    def interactor_mock_response():
        from ib_tasks.tests.factories.presenter_dtos \
            import ProjectTemplateFieldsDTOFactory
        ProjectTemplateFieldsDTOFactory.reset_sequence()
        ProjectTemplateDTOFactory.reset_sequence(1)
        TaskTemplateGofsDTOFactory.reset_sequence(1)
        FieldNameDTOFactory.reset_sequence(1)
        template_fields = ProjectTemplateFieldsDTOFactory(
            task_template_dtos=[ProjectTemplateDTOFactory()],
            task_template_gofs_dtos=[TaskTemplateGofsDTOFactory()],
            fields_dto=FieldNameDTOFactory.create_batch(2)
        )
        return template_fields

    @pytest.fixture()
    def template_path_mock(self, mocker):
        path = 'ib_tasks.interactors.get_templates_fields_to_project_ids.GetProjectsTemplatesFieldsInteractor' \
               '.get_task_templates'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_given_invalid_project_id_raises_exception(
            self, interactor, template_path_mock):

        # Arrange
        from ib_tasks.exceptions.adapter_exceptions \
            import InvalidProjectIdsException
        project_id = 'FIN_MAN'
        project_ids = [project_id]
        template_path_mock.side_effect = \
            InvalidProjectIdsException(invalid_project_ids=project_ids)
        user_id = 'user_1'
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
            import FilterPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(FilterPresenterInterface)

        # Act
        interactor.get_task_templates_fields_wrapper(
            user_id=user_id, project_id=project_id, presenter=presenter
        )

        # Assert
        obj = presenter.get_response_for_invalid_project_id.call_args.kwargs
        assert obj['err'].invalid_project_ids == project_ids

    @pytest.fixture()
    def presenter(self):
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
            import FilterPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(FilterPresenterInterface)
        return presenter

    def test_user_not_in_project_raises_exception(
            self, interactor, template_path_mock, presenter
    ):
        from ib_tasks.exceptions.adapter_exceptions \
            import UserIsNotInProjectsException
        project_id = 'FIN_MAN'
        project_ids = [project_id]
        template_path_mock.side_effect = \
            UserIsNotInProjectsException(project_ids=project_ids)
        user_id = 'user_1'

        # Act
        interactor.get_task_templates_fields_wrapper(
            user_id=user_id, project_id=project_id, presenter=presenter
        )

        # Assert
        presenter.get_response_for_user_not_in_project.assert_called_once()

    def test_return_task_templates_fields_details(
            self, interactor, interactor_mock_response, template_path_mock):

        # Arrange
        template_path_mock.return_value = interactor_mock_response
        user_id = "user_1"
        project_id = 'FIN_MAN'
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
            import FilterPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(FilterPresenterInterface)

        # Act
        interactor.get_task_templates_fields_wrapper(
            user_id=user_id, project_id=project_id, presenter=presenter
        )

        # Assert
        presenter.get_response_for_get_task_templates_fields\
            .assert_called_once_with(task_template_fields=interactor_mock_response)
