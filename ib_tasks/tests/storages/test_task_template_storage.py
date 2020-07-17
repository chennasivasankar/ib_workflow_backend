import pytest
from ib_tasks.storages.task_storage_implementation import \
    TaskStorageImplementation
from ib_tasks.tests.factories.models import TaskTemplateFactory, GoFFactory


class TestTaskStorageImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()
        GoFFactory.reset_sequence()

    @pytest.mark.django_db
    def test_check_is_template_exists_with_invalid_template_id_returns_false(
            self):
        #Arrange
        template_id = "Template_1"
        storage = TaskStorageImplementation()

        #Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        #Assert
        assert is_template_exists is False

    @pytest.mark.django_db
    def test_check_is_template_exists_with_valid_template_id_returns_true(
            self):
        #Arrange
        template_id = "template_1"
        storage = TaskStorageImplementation()
        TaskTemplateFactory.create_batch(size=1)

        #Act
        is_template_exists = \
            storage.check_is_template_exists(template_id=template_id)

        #Assert
        assert is_template_exists is True


    @pytest.mark.django_db
    def test_create_task_template(self):
        #Arrange
        template_id = "template_1"
        template_name = "Task Template 1"
        storage = TaskStorageImplementation()

        #Act
        storage.create_task_template(
            template_id=template_id, template_name=template_name
        )

        #Assert
        from ib_tasks.models.task_template import TaskTemplate
        task_template = TaskTemplate.objects.get(template_id=template_id)

        assert task_template.template_id == template_id
        assert task_template.name == template_name

    @pytest.mark.django_db
    def test_add_gofs_to_task_template(self):
        #Arrange
        template_id = "template_1"
        TaskTemplateFactory.create_batch(size=1)
        GoFFactory.create_batch(size=2, task_template=None)

        import factory
        from ib_tasks.models.gof import GoF
        gof_ids_list = GoF.objects.all().values_list('gof_id', flat=True)

        from ib_tasks.tests.factories.interactor_dtos import \
            GoFIdAndOrderDTOFactory
        gof_id_and_order_dtos = GoFIdAndOrderDTOFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids_list), order=3
        )
        storage = TaskStorageImplementation()

        #Act
        storage.add_gofs_to_task_template(
            template_id=template_id,
            gof_id_and_order_dtos=gof_id_and_order_dtos
        )

        #Assert
        gof_objects = GoF.objects.filter(gof_id__in = gof_ids_list)
        assert gof_objects[0].task_template_id == template_id
        assert gof_objects[0].order == 3
        assert gof_objects[1].task_template_id == template_id
        assert gof_objects[1].order == 3

    @pytest.mark.django_db
    def test_get_existing_gof_ids_of_template(self):
        #Arrange
        template_id = "template_1"
        GoFFactory.create_batch(size=2, task_template_id = template_id)
        storage = TaskStorageImplementation()

        #Act
        existing_gof_ids_of_template = \
            storage.get_existing_gof_ids_of_template(
                template_id=template_id
            )

        #Assert
        assert existing_gof_ids_of_template == ['gof_1', 'gof_2']
