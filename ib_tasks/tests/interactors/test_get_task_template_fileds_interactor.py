mport pytest
import factory

from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface import TaskTemplateFieldsDto
from ib_tasks.interactors.presenter_interfaces.get_task_templates_presenter_interface import CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldNameDTO
from ib_tasks.tests.factories.storage_dtos import TaskTemplateDTOFactory, StageIdWithTemplateIdDTOFactory, \
    ActionWithStageIdDTOFactory, GoFDTOFactory, FieldDTOFactory, FieldPermissionDTOFactory, GoFToTaskTemplateDTOFactory

import factory
import pytest

from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import \
    TaskTemplateFieldsDto
from ib_tasks.interactors.presenter_interfaces\
    .get_task_templates_presenter_interface import \
    CompleteTaskTemplatesDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldNameDTO
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
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
            import TaskTemplateStorageInterface
        from unittest.mock import create_autospec
        field_storage = create_autospec(FieldsStorageInterface)
        gof_storage = create_autospec(GoFStorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        task_template_storage = create_autospec(TaskTemplateStorageInterface)
        from ib_tasks.interactors.get_task_templates_fields_interactor \
            import GetTaskTemplatesFieldsInteractor
        interactor = GetTaskTemplatesFieldsInteractor(
            field_storage=field_storage,
            gof_storage=gof_storage,
            task_storage=task_storage,
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
    def interactor_mock():

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(size=2)
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(size=4)
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )
        return complete_task_templates_dto

    def response(self):
        TaskTemplateDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        return TaskTemplateFieldsDto(
            task_template_dtos=TaskTemplateDTOFactory.create_batch(size=2),
            gofs_of_task_templates_dtos=GoFToTaskTemplateDTOFactory.create_batch(size=2),
            fields_dto=[
                FieldNameDTO(field_id='field0', gof_id='FIN_VENDOR_BASIC_DETAILS', field_display_name='field name'),
                FieldNameDTO(field_id='field1', gof_id='FIN_VENDOR_BASIC_DETAILS', field_display_name='field name')]
        )

    def test_return_task_templates_fields_details(
            self, interactor, mocker, interactor_mock):

        # Arrange
        path = 'ib_tasks.interactors.get_task_templates_interactor.GetTaskTemplatesInteractor' \
               '.get_task_templates'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = interactor_mock
        user_id = "user_1"
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
            import FilterPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(FilterPresenterInterface)

        # Act

        interactor.get_task_templates_fields_wrapper(
            user_id=user_id, presenter=presenter
        )

        # Assert
        presenter.get_response_for_get_task_templates_fields.assert_called_once_with(
            task_template_fields=self.response()
        )