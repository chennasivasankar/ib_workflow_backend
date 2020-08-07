import pytest

from ib_tasks.interactors.task_template_dtos import CreateTemplateDTO
from ib_tasks.models.task_template import TaskTemplate


class TestCreateTaskTemplate:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskTemplateWithTransitionFactory
        TaskTemplateWithTransitionFactory.reset_sequence()

    @pytest.fixture
    def create_template_interactor(self):
        from ib_tasks.interactors.create_template_interactor import \
            CreateTemplateInteractor
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()
        template_interactor = CreateTemplateInteractor(
            task_template_storage=task_template_storage
        )
        return template_interactor

    @pytest.mark.django_db
    def test_with_invalid_template_id_raises_exception(
            self, create_template_interactor, snapshot):
        # Arrange
        template_id = "  "
        template_name = "IB"
        is_transition_template = True

        create_template_dto = CreateTemplateDTO(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            create_template_interactor.create_template_wrapper(
                create_template_dto=create_template_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_invalid_template_name_raises_exception(
            self, create_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "   "
        is_transition_template = True

        create_template_dto = CreateTemplateDTO(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            create_template_interactor.create_template_wrapper(
                create_template_dto=create_template_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_valid_data(self, create_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "Template 1"
        is_transition_template = True
        create_template_dto = CreateTemplateDTO(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Act
        create_template_interactor.create_template_wrapper(
            create_template_dto=create_template_dto
        )

        # Assert
        template = \
            TaskTemplate.objects.filter(template_id=template_id).first()

        snapshot.assert_match(template.template_id, 'template_id')
        snapshot.assert_match(template.name, 'template_name')
        snapshot.assert_match(
            template.is_transition_template, 'is_transition_template'
        )

    @pytest.mark.django_db
    def test_with_existing_template_id_but_different_name_updates_template(
            self, create_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "iBHubs 1"
        is_transition_template = False
        from ib_tasks.tests.factories.models import TaskTemplateWithTransitionFactory
        TaskTemplateWithTransitionFactory(template_id=template_id, name=template_name)

        create_template_dto = CreateTemplateDTO(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Act
        create_template_interactor.create_template_wrapper(
            create_template_dto=create_template_dto
        )

        # Assert
        template = \
            TaskTemplate.objects.filter(template_id=template_id).first()

        snapshot.assert_match(template.template_id, 'template_id')
        snapshot.assert_match(template.name, 'template_name')
        snapshot.assert_match(
            template.is_transition_template, 'is_transition_template'
        )

    @pytest.mark.django_db
    def test_with_existing_template_id_but_different_is_transition_template_field_updates_template(
            self, create_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        template_name = "iBHubs 1"
        is_transition_template = True
        from ib_tasks.tests.factories.models import TaskTemplateWithTransitionFactory
        TaskTemplateWithTransitionFactory(template_id=template_id, name=template_name)

        create_template_dto = CreateTemplateDTO(
            template_id=template_id, template_name=template_name,
            is_transition_template=is_transition_template
        )

        # Act
        create_template_interactor.create_template_wrapper(
            create_template_dto=create_template_dto
        )

        # Assert
        template = \
            TaskTemplate.objects.filter(template_id=template_id).first()

        snapshot.assert_match(template.template_id, 'template_id')
        snapshot.assert_match(template.name, 'template_name')
        snapshot.assert_match(
            template.is_transition_template, 'is_transition_template'
        )
