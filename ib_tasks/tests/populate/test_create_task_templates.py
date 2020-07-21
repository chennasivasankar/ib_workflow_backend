import pytest
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO

class TestCreateTaskTemplate:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory.reset_sequence()

    @pytest.fixture
    def create_task_templates_interactor(self):
        from ib_tasks.interactors.task_template_interactor import \
            TaskTemplateInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation

        task_storage = TasksStorageImplementation()
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage
        )
        return task_template_interactor

    @pytest.mark.django_db
    def test_with_invalid_template_id_raises_exception(
            self, create_task_templates_interactor, snapshot):
        #Arrange
        template_id = "  "
        template_name = "IB"

        create_task_template_dto= CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidValueForField

        #Asssert
        with pytest.raises(InvalidValueForField) as err:
            create_task_templates_interactor.\
                create_task_template_wrapper(
                    create_task_template_dto=create_task_template_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_invalid_template_name_raises_exception(
            self, create_task_templates_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "   "
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidValueForField

        # Asssert
        with pytest.raises(InvalidValueForField) as err:
            create_task_templates_interactor. \
                create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_valid_data(
            self, create_task_templates_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "Template 1"
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )

        #Act
        create_task_templates_interactor. \
            create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        #Assert
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.filter(template_id=template_id).first()

        snapshot.assert_match(task_template.template_id, 'template_id')
        snapshot.assert_match(task_template.name, 'template_name')

    @pytest.mark.django_db
    def test_with_existing_template_id_but_different_name_updates_template(
            self, create_task_templates_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "iBHubs 1"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory()

        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )

        #Act
        create_task_templates_interactor. \
            create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        #Assert
        from ib_tasks.models.task_template import TaskTemplate
        task_template = \
            TaskTemplate.objects.filter(template_id=template_id).first()

        snapshot.assert_match(task_template.template_id, 'template_id')
        snapshot.assert_match(task_template.name, 'template_name')
