import pytest
import factory
from ib_tasks.interactors.presenter_interfaces. \
    get_task_templates_presenter_interface import CompleteTaskTemplatesDTO
from ib_tasks.presenters.get_task_templates_presenter_implementation import \
    GetTaskTemplatesPresenterImplementation
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, ActionWithStageIdDTOFactory, \
    UserFieldPermissionDTOFactory, FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, \
    FieldPermissionDTOFactory, StageIdWithTemplateIdDTOFactory


class TestGetTaskTemplatesPresenterImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        ActionWithStageIdDTOFactory.reset_sequence(1)
        FieldDTOFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        UserFieldPermissionDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.reset_sequence()
        FieldPermissionDTOFactory.is_field_writable.reset()
        StageIdWithTemplateIdDTOFactory.reset_sequence(1)

    def test_when_complete_task_template_details_exists(self, snapshot):
        # Arrange
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ["field_1", "field_2", "field_3", "field_4"]

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(
                size=2, template_id="template_1"
            )
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(
                size=2, stage_id=factory.Iterator([1, 2])
            )
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, field_id=factory.Iterator(expected_field_ids),
            gof_id=factory.Iterator(expected_gof_ids)
        )
        UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        # Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_when_no_task_templates_exists_returns_empty_list(self, snapshot):
        # Arrange
        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=[],
            stage_id_with_template_id_dtos=[],
            action_with_stage_id_dtos=[],
            gof_dtos=[],
            gofs_of_task_templates_dtos=[],
            field_with_permissions_dtos=[]
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        # Assert
        import json
        response_content = json.loads(presenter_response_object.content)
        snapshot.assert_match(response_content, 'task_templates')

    def test_when_no_gofs_exists_returns_empty_gofs_list(self, snapshot):
        # Arrange
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(
                size=2, template_id="template_1"
            )
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(
                size=2, stage_id=factory.Iterator([1, 2])
            )

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=[],
            gofs_of_task_templates_dtos=[],
            field_with_permissions_dtos=[]
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        # Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_when_no_actions_for_user_exists_returns_empty_actions_list(
            self, snapshot):
        # Arrange
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ["field_1", "field_2", "field_3", "field_4"]

        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, field_id=factory.Iterator(expected_field_ids),
            gof_id=factory.Iterator(expected_gof_ids)
        )
        UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)
        field_with_permissions_dtos = \
            FieldPermissionDTOFactory.create_batch(
                size=2, field_dto=factory.Iterator(field_dtos),
                is_field_writable=factory.Iterator([False, True])
            )

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            stage_id_with_template_id_dtos=[],
            action_with_stage_id_dtos=[],
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=field_with_permissions_dtos
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        # Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_when_no_fields_exists_returns_empty_fields_list(self, snapshot):
        # Arrange
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        stage_id_with_template_id_dtos = \
            StageIdWithTemplateIdDTOFactory.create_batch(
                size=2, template_id="template_1"
            )
        action_with_stage_id_dtos = \
            ActionWithStageIdDTOFactory.create_batch(
                size=2, stage_id=factory.Iterator([1, 2])
            )
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            stage_id_with_template_id_dtos=stage_id_with_template_id_dtos,
            action_with_stage_id_dtos=action_with_stage_id_dtos,
            gof_dtos=gof_dtos,
            gofs_of_task_templates_dtos=gof_to_task_template_dtos,
            field_with_permissions_dtos=[]
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        # Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_raise_task_templates_does_not_exists_exception(self, snapshot):
        # Arrange
        presenter = GetTaskTemplatesPresenterImplementation()

        # Act
        response_object = \
            presenter.raise_task_templates_does_not_exists_exception()

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')
