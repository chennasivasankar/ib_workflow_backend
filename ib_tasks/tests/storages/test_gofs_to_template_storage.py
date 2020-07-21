import pytest
from ib_tasks.tests.factories.models import TaskTemplateWith2GoFsFactory


class TestGoFsToTaskTemplateStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory.reset_sequence()
        from ib_tasks.tests.factories.models import GoFFactory
        GoFFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        GoFWithOrderAndAddAnotherDTOFactory.reset_sequence()

    @pytest.mark.django_db
    def test_get_existing_gof_ids_of_template(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        expected_gof_ids = ['gof_1', 'gof_2']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        #Act
        existing_gof_ids_of_template = \
            storage.get_existing_gof_ids_of_template(template_id=template_id)

        #Assert
        assert existing_gof_ids_of_template == expected_gof_ids

    @pytest.mark.django_db
    def test_get_valid_gof_ids_in_given_gof_ids(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        gof_ids = ['gof_1', 'gof_3']
        expected_gof_ids = ['gof_1']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        #Act
        valid_gof_ids = \
            storage.get_valid_gof_ids_in_given_gof_ids(gof_ids=gof_ids)

        #Assert
        assert valid_gof_ids == expected_gof_ids

    @pytest.mark.django_db
    def test_add_gofs_to_template(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        from ib_tasks.tests.factories.models import GoFFactory
        GoFFactory.create_batch(size=2)
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)

        #Act
        storage.add_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos
        )

        #Assert
        from ib_tasks.models.gof_to_task_template import GoFToTaskTemplate
        gof_to_task_template_objs = \
            GoFToTaskTemplate.objects.filter(task_template_id=template_id)

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

    @pytest.mark.django_db
    def test_update_gofs_to_template(self, storage):
        #Arrange
        template_id = "FIN_VENDOR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=5, enable_add_another_gof=True
        )
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        #Act
        storage.update_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos
        )

        #Assert
        from ib_tasks.models.gof_to_task_template import GoFToTaskTemplate
        gof_to_task_template_objs = \
            GoFToTaskTemplate.objects.filter(task_template_id=template_id)

        assert gof_to_task_template_objs[0].order == \
               gof_dtos[0].order
        assert gof_to_task_template_objs[0].enable_add_another_gof == \
               gof_dtos[0].enable_add_another_gof
        assert gof_to_task_template_objs[1].order == gof_dtos[0].order
        assert gof_to_task_template_objs[1].enable_add_another_gof == \
               gof_dtos[1].enable_add_another_gof
