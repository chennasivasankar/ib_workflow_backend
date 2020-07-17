import pytest
from ib_tasks.storages.task_storage_implementation import \
    TaskStorageImplementation
from ib_tasks.tests.factories.models import TaskTemplateFactory


class TestTaskStorageImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.reset_sequence()

        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory
        GlobalConstantsDTOFactory.reset_sequence()

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
    def test_get_constant_names_of_existing_global_constants_of_template_returns_constant_names(
            self):
        #Arrange
        template_id = "template_1"
        storage = TaskStorageImplementation()
        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        expected_constant_names = ['constant_1', 'constant_2', 'constant_3']

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.create_batch(
            size=3, task_template_id=template_id
        )

        #Act
        global_constants_of_template = storage.\
            get_constant_names_of_existing_global_constants_of_template(
                template_id=template_id
            )

        #Assert
        assert global_constants_of_template == expected_constant_names

    @pytest.mark.django_db
    def test_get_constant_names_of_existing_global_constants_of_template_when_no_constants_returns_empty_list(
            self):
        #Arrange
        template_id = "template_1"
        storage = TaskStorageImplementation()
        TaskTemplateFactory.create_batch(size=1, template_id=template_id)

        #Act
        global_constants_of_template = storage.\
            get_constant_names_of_existing_global_constants_of_template(
                template_id=template_id
            )

        #Assert
        assert global_constants_of_template == []

    @pytest.mark.django_db
    def test_create_global_constants_to_template(self):
        #Arrange
        template_id = "template_1"
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory

        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        storage = TaskStorageImplementation()

        #Act
        storage.create_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

        #Assert
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
