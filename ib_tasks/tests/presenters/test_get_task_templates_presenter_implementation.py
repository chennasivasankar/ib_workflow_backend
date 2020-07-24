import pytest
from ib_tasks.interactors.presenter_interfaces.\
    get_task_templates_presenter_interface import CompleteTaskTemplatesDTO
from ib_tasks.presenters.get_task_templates_presenter_implementation import \
    GetTaskTemplatesPresenterImplementation
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, ActionsOfTemplateDTOFactory, \
    UserFieldPermissionDTOFactory, FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory


class TestGetTaskPresenterImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateDTOFactory.reset_sequence()
        ActionsOfTemplateDTOFactory.reset_sequence()
        FieldDTOFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        UserFieldPermissionDTOFactory.reset_sequence()
        GoFToTaskTemplateDTOFactory.reset_sequence()

    def test_when_complete_task_template_details_exists(self, snapshot):
        #Arrange
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ["field_1", "field_2", "field_3", "field_4"]
        import factory
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(
                size=2, template_id="template_1"
            )
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, field_id=factory.Iterator(expected_field_ids),
            gof_id=factory.Iterator(expected_gof_ids)
        )
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        #Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        #Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_when_no_task_templates_exists_returns_empty_list(self, snapshot):
        #Arrange
        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=[],
            actions_of_templates_dtos=[],
            gof_dtos=[],
            gofs_to_task_templates_dtos=[],
            field_dtos=[],
            user_field_permission_dtos=[]
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        #Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        #Assert
        import json
        response_content = json.loads(presenter_response_object.content)
        snapshot.assert_match(response_content, 'task_templates')

    def test_when_no_gofs_exists_returns_empty_gofs_list(self, snapshot):
        #Arrange
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(
                size=2, template_id="template_1"
            )

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=[],
            gofs_to_task_templates_dtos=[],
            field_dtos=[],
            user_field_permission_dtos=[]
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        #Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        #Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1

    def test_when_no_actions_for_user_exists_returns_empty_actions_list(self, snapshot):
        # Arrange
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_ids = ["field_1", "field_2", "field_3", "field_4"]
        import factory
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        field_dtos = FieldDTOFactory.create_batch(
            size=4, field_id=factory.Iterator(expected_field_ids),
            gof_id=factory.Iterator(expected_gof_ids)
        )
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=[],
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=field_dtos,
            user_field_permission_dtos=user_field_permission_dtos
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
        #Arrange
        task_template_dtos = TaskTemplateDTOFactory.create_batch(size=2)
        actions_of_template_dtos = \
            ActionsOfTemplateDTOFactory.create_batch(
                size=2, template_id="template_1"
            )
        gof_dtos = GoFDTOFactory.create_batch(size=2)
        user_field_permission_dtos = \
            UserFieldPermissionDTOFactory.create_batch(size=4)
        gof_to_task_template_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(size=2)

        complete_task_templates_dto = CompleteTaskTemplatesDTO(
            task_template_dtos=task_template_dtos,
            actions_of_templates_dtos=actions_of_template_dtos,
            gof_dtos=gof_dtos,
            gofs_to_task_templates_dtos=gof_to_task_template_dtos,
            field_dtos=[],
            user_field_permission_dtos=user_field_permission_dtos
        )
        presenter = GetTaskTemplatesPresenterImplementation()

        #Act
        presenter_response_object = presenter.get_task_templates_response(
            complete_task_templates_dto=complete_task_templates_dto
        )

        #Assert
        import json
        response_content = json.loads(presenter_response_object.content)

        counter = 1
        for task_template in response_content['task_templates']:
            snapshot.assert_match(
                task_template, 'task_template_{}'.format(counter)
            )
            counter = counter + 1
