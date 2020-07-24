import pytest


@pytest.mark.django_db
class TestGetTaskTemplates:
    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.storage_dtos import \
            ActionsOfTemplateDTOFactory
        from ib_tasks.tests.factories.models import StageModelFactory, \
            StageActionFactory, GoFToTaskTemplateFactory, GoFFactory, \
            TaskTemplateFactory, FieldFactory

        StageModelFactory.reset_sequence()
        ActionsOfTemplateDTOFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        storage = TasksStorageImplementation()
        return storage

    def test_get_task_templates_dtos(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        from ib_tasks.interactors.storage_interfaces.task_templates_dtos \
            import TaskTemplateDTO
        expected_output = [
            TaskTemplateDTO(
                template_id='template_1', template_name='Template 1'
            ),
            TaskTemplateDTO(
                template_id='template_2', template_name='Template 2'
            )
        ]

        TaskTemplateFactory.create_batch(size=2)

        # Act
        result = storage.get_task_templates_dtos()

        # Assert
        assert result == expected_output

    def test_get_actions_of_templates_dtos(self, storage):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.actions_dtos \
            import ActionsOfTemplateDTO
        from ib_tasks.tests.factories.models import \
            StageModelFactory, StageActionFactory
        expected_output = [
            ActionsOfTemplateDTO(
                template_id='task_template_id_2',
                action_id=1, button_text='hey',
                button_color='#fafafa'
            ),
            ActionsOfTemplateDTO(
                template_id='task_template_id_3',
                action_id=2, button_text='hey',
                button_color='#fafafa'
            )
        ]

        StageModelFactory.create_batch(size=2)
        StageActionFactory.create_batch(size=2)

        # Act
        result = storage.get_actions_of_templates_dtos()

        # Assert
        assert result == expected_output

    def test_get_gof_ids_with_read_permission_for_user(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import GoFRoleFactory
        expected_output = ['gof_1', 'gof_2']
        expected_roles = ['ROLE-1']
        GoFRoleFactory.create_batch(size=2)

        # Act
        result = storage.get_gof_ids_with_read_permission_for_user(
            roles=expected_roles
        )

        # Assert
        assert result == expected_output

    def test_get_gofs_to_task_templates_from_permitted_gofs(self, storage):
        from ib_tasks.tests.factories.models import \
            GoFToTaskTemplateFactory, GoFFactory
        from ib_tasks.interactors.storage_interfaces.gof_dtos import \
            GoFToTaskTemplateDTO
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_gof_to_task_templates_dtos = [
            GoFToTaskTemplateDTO(gof_id='gof_1', template_id='template_1',
                                 order=0, enable_add_another=True),
            GoFToTaskTemplateDTO(gof_id='gof_2', template_id='template_2',
                                 order=1, enable_add_another=False)]

        import factory
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_objs)
        )

        # Act
        result = storage.get_gofs_to_task_templates_from_permitted_gofs(
            gof_ids=expected_gof_ids
        )

        # Assert
        assert result == expected_gof_to_task_templates_dtos

    def test_get_gofs_details_dtos(self, storage):
        from ib_tasks.tests.factories.models import GoFFactory
        from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_gof_dtos = [
            GoFDTO(gof_id='gof_1', gof_display_name='GOF_DISPLAY_NAME-0',
                   max_columns=2),
            GoFDTO(gof_id='gof_2', gof_display_name='GOF_DISPLAY_NAME-1',
                   max_columns=2)]

        import factory
        GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )

        # Act
        result = storage.get_gofs_details_dtos(gof_ids=expected_gof_ids)

        # Assert
        assert result == expected_gof_dtos

    def test_get_fields_of_gofs_in_dtos(self, storage):
        from ib_tasks.tests.factories.models import GoFFactory, FieldFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import FieldDTO
        from ib_tasks.constants.enum import FieldTypes
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_field_dtos = [FieldDTO(gof_id='gof_1', field_id='FIELD_ID-0',
                                        field_display_name='DISPLAY_NAME-0',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None),
                               FieldDTO(gof_id='gof_2', field_id='FIELD_ID-1',
                                        field_display_name='DISPLAY_NAME-1',
                                        field_type=FieldTypes.PLAIN_TEXT.value,
                                        field_values=None, required=True,
                                        help_text=None, tooltip=None,
                                        placeholder_text=None,
                                        error_message=None,
                                        allowed_formats=None,
                                        validation_regex=None)]

        import factory
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        FieldFactory.create_batch(size=2,
                                  gof=factory.Iterator(gof_objs))

        # Act
        result = storage.get_fields_of_gofs_in_dtos(gof_ids=expected_gof_ids)

        # Assert
        assert result == expected_field_dtos

    def test_get_user_field_permission_dtos(self, storage):
        from ib_tasks.tests.factories.models import FieldFactory, \
            FieldRoleFactory
        from ib_tasks.interactors.storage_interfaces.fields_dtos \
            import UserFieldPermissionDTO
        from ib_tasks.constants.enum import PermissionTypes
        expected_field_ids = ['field_1', 'field_2']
        expected_user_field_permission_dtos = [
            UserFieldPermissionDTO(field_id='field_1',
                                   permission_type=PermissionTypes.READ.value)]

        import factory
        field_objs = FieldFactory.create_batch(size=2,
                                               field_id=factory.Iterator(
                                                   expected_field_ids))
        FieldRoleFactory.create_batch(size=2,
                                      field=factory.Iterator(field_objs))

        # Act
        result = storage.get_user_field_permission_dtos(
            field_ids=expected_field_ids, roles=['FIN_PAYMENT_REQUESTER'])

        # Assert
        assert result == expected_user_field_permission_dtos
