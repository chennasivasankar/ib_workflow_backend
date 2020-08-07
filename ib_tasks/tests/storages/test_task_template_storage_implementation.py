import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateWith2GoFsFactory


@pytest.mark.django_db
class TestTaskTemplateStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        return TaskTemplateStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory, GlobalConstantsDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory, \
            GlobalConstantFactory, GoFToTaskTemplateFactory
        GoFWithOrderAndAddAnotherDTOFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GoFFactory.reset_sequence()
        GlobalConstantFactory.reset_sequence()
        GlobalConstantsDTOFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()

    def test_get_valid_template_ids_in_given_template_ids(self, storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_ids = [task_template.template_id, "FIN_VENDOR"]
        expected_valid_template_ids = [task_template.template_id]

        # Act
        actual_valid_template_ids = \
            storage.get_valid_template_ids_in_given_template_ids(template_ids)

        # Assert
        assert expected_valid_template_ids == actual_valid_template_ids

    def test_get_gofs_to_templates_from_permitted_gofs(self, storage):
        # Arrange
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
        result = storage.get_gofs_to_templates_from_permitted_gofs(
            gof_ids=expected_gof_ids
        )

        # Assert
        assert result == expected_gof_to_task_templates_dtos

    def test_get_task_templates_dtos(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        from ib_tasks.interactors.storage_interfaces.task_templates_dtos \
            import TemplateDTO
        expected_output = [
            TemplateDTO(
                template_id='template_1', template_name='Template 1'
            ),
            TemplateDTO(
                template_id='template_2', template_name='Template 2'
            )
        ]

        TaskTemplateFactory.create_batch(size=2)

        # Act
        result = storage.get_task_templates_dtos()

        # Assert
        assert result == expected_output

    def test_check_is_template_exists_with_invalid_template_id_returns_false(
            self, storage):
        # Arrange
        template_id = "FIN_VENDOR"

        # Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        # Assert
        assert is_template_exists is False

    def test_get_constant_names_of_existing_global_constants_of_template_returns_constant_names(
            self, storage):
        # Arrange
        template_id = "FIN_PR"
        task_template = TaskTemplateFactory(template_id=template_id)
        expected_constant_names = ['constant_1', 'constant_2', 'constant_3']

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.create_batch(
            size=3, task_template=task_template
        )

        # Act
        global_constants_of_template = storage. \
            get_constant_names_of_existing_global_constants_of_template(
            template_id=template_id
        )

        # Assert
        assert global_constants_of_template == expected_constant_names

    def test_get_constant_names_of_existing_global_constants_of_template_when_no_constants_returns_empty_list(
            self, storage):
        # Arrange
        template_id = "template_1"
        TaskTemplateFactory(template_id=template_id)

        # Act
        global_constants_of_template = storage. \
            get_constant_names_of_existing_global_constants_of_template(
            template_id=template_id
        )

        # Assert
        assert global_constants_of_template == []

    def test_create_global_constants_to_template(self, storage):
        # Arrange

        template_id = "FIN_PR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory

        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)

        # Act
        storage.create_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

        # Assert
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = \
            GlobalConstant.objects.filter(task_template_id=template_id)

        assert global_constants_objs[0].task_template_id == template_id
        assert global_constants_objs[0].name == \
               global_constants_dtos[0].constant_name
        assert global_constants_objs[0].value == \
               global_constants_dtos[0].value
        assert global_constants_objs[1].task_template_id == template_id
        assert global_constants_objs[1].name == \
               global_constants_dtos[1].constant_name
        assert global_constants_objs[1].value == \
               global_constants_dtos[1].value

    def test_update_global_constants_to_template(self, storage):
        # Arrange

        template_id = "FIN_PR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory
        from ib_tasks.tests.factories.models import GlobalConstantFactory

        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        GlobalConstantFactory.create_batch(
            size=1, task_template_id=template_id, value=100000,
            name="Constant_1"
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=1)

        # Act
        storage.update_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

        # Assert
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = \
            GlobalConstant.objects.filter(task_template_id=template_id)

        assert global_constants_objs[0].task_template_id == template_id
        assert global_constants_objs[0].name == \
               global_constants_dtos[0].constant_name
        assert global_constants_objs[0].value == \
               global_constants_dtos[0].value

    def test_check_is_template_exists_with_valid_template_id_returns_true(
            self, storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_id = task_template.template_id

        # Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        # Assert
        assert is_template_exists is True

    def test_create_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        template_name = "Task Template 1"
        is_transition_template = True

        # Act
        storage.create_template(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Assert
        from ib_tasks.models.task_template import TaskTemplate
        template = TaskTemplate.objects.get(template_id=template_id)

        assert template.template_id == template_id
        assert template.name == template_name
        assert template.is_transition_template == is_transition_template

    def test_update_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        template_name = "iB Template"
        is_transition_template = True
        TaskTemplateFactory(
            template_id=template_id, name=template_name
        )

        # Act
        storage.update_template(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Assert
        from ib_tasks.models.task_template import TaskTemplate
        template = TaskTemplate.objects.get(template_id=template_id)

        assert template.template_id == template_id
        assert template.name == template_name
        assert template.is_transition_template == is_transition_template

    def test_get_existing_gof_ids_of_template(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import \
            TaskTemplateWith2GoFsFactory

        template_id = "FIN_VENDOR"
        expected_gof_ids = ['gof_1', 'gof_2']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        # Act
        existing_gof_ids_of_template = \
            storage.get_existing_gof_ids_of_template(template_id=template_id)

        # Assert
        assert existing_gof_ids_of_template == expected_gof_ids

    def test_add_gofs_to_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)

        from ib_tasks.tests.factories.models import GoFFactory
        GoFFactory.create_batch(size=2)

        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)

        # Act
        storage.add_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos
        )

        # Assert
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gof_to_task_template_objs = \
            TaskTemplateGoFs.objects.filter(task_template_id=template_id)

        assert gof_to_task_template_objs[0].task_template_id == template_id
        assert gof_to_task_template_objs[0].gof_id == \
               gof_dtos[0].gof_id
        assert gof_to_task_template_objs[0].order == \
               gof_dtos[0].order
        assert gof_to_task_template_objs[0].enable_add_another_gof == \
               gof_dtos[0].enable_add_another_gof
        assert gof_to_task_template_objs[1].task_template_id == template_id
        assert gof_to_task_template_objs[1].gof_id == \
               gof_dtos[1].gof_id
        assert gof_to_task_template_objs[1].order == \
               gof_dtos[1].order
        assert gof_to_task_template_objs[1].enable_add_another_gof == \
               gof_dtos[1].enable_add_another_gof

    def test_update_gofs_to_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=5, enable_add_another_gof=True
        )
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        # Act
        storage.update_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos
        )

        # Assert
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gof_to_task_template_objs = \
            TaskTemplateGoFs.objects.filter(task_template_id=template_id)

        assert gof_to_task_template_objs[0].order == \
               gof_dtos[0].order
        assert gof_to_task_template_objs[0].enable_add_another_gof == \
               gof_dtos[0].enable_add_another_gof
        assert gof_to_task_template_objs[1].order == gof_dtos[0].order
        assert gof_to_task_template_objs[1].enable_add_another_gof == \
               gof_dtos[1].enable_add_another_gof

    def test_get_transition_template_dto(self, storage):
        # Arrange
        transition_template = TaskTemplateFactory()

        # Act
        transition_template_dto = storage.get_transition_template_dto(
            transition_template_id=transition_template.template_id)

        # Assert
        assert transition_template_dto.template_id == \
               transition_template.template_id
        assert transition_template_dto.template_name == \
               transition_template.name

    def test_check_is_transition_template_exists_with_invalid_transition_template_id_returns_false(
            self, storage):
        # Arrange
        transition_template_id = "template_1"

        # Act
        is_transition_template_exists = \
            storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)

        # Assert
        assert is_transition_template_exists is False

    def test_check_is_transition_template_exists_with_valid_transition_template_id_returns_true(
            self, storage):
        # Arrange
        transition_template = TaskTemplateFactory(is_transition_template=True)
        transition_template_id = transition_template.template_id

        # Act
        is_transition_template_exists = \
            storage.check_is_transition_template_exists(
                transition_template_id=transition_template_id)

        # Assert
        assert is_transition_template_exists is True

    def test_get_gofs_to_template_from_permitted_gofs(self, storage):
        # Arrange
        import factory
        from ib_tasks.tests.factories.models import \
            GoFToTaskTemplateFactory, GoFFactory
        from ib_tasks.tests.factories.storage_dtos import \
            GoFToTaskTemplateDTOFactory
        template_id = "template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_gof_to_task_templates_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(
                size=2, gof_id=factory.Iterator(expected_gof_ids),
                template_id=template_id
            )

        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids),
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_objs),
            task_template_id=template_id
        )

        # Act
        result = storage.get_gofs_to_template_from_permitted_gofs(
            gof_ids=expected_gof_ids, template_id=template_id
        )

        # Assert
        assert result == expected_gof_to_task_templates_dtos
