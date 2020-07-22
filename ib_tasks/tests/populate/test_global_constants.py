import pytest
from ib_tasks.tests.factories.interactor_dtos import \
    GlobalConstantsDTOFactory
from ib_tasks.interactors.dtos import GlobalConstantsWithTemplateIdDTO

class TestGlobalConstants:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GlobalConstantFactory
        GlobalConstantsDTOFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GlobalConstantFactory.reset_sequence()

    @pytest.fixture
    def global_constants_interactor(self):
        from ib_tasks.interactors.global_constants_interactor import \
            GlobalConstantsInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation

        task_storage = TasksStorageImplementation()
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage
        )
        return global_constants_interactor

    @pytest.mark.django_db
    def test_with_invalid_template_raises_exception(
            self, global_constants_interactor, snapshot):
        #Arrange
        template_id = "FIN_MAN"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.task_custom_exceptions import TemplateDoesNotExists

        #Asssert
        with pytest.raises(TemplateDoesNotExists) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                    global_constants_with_template_id_dto=global_constants_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_template_id_is_empty_raises_exception(
            self, global_constants_interactor, snapshot):
        # Arrange
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=" ",
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_constant_name_is_empty_raises_exception(
            self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name=" "
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_invalid_value_for_value_field_raises_exception(
            self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, value=-1
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.fields_custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_duplicate_constant_names_raises_exception(
            self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name="iB_Hubs"
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.constants_custom_exceptions import DuplicateConstantNames

        # Assert
        with pytest.raises(DuplicateConstantNames) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_valid_data(self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "TEMPLATE_ID-0"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        TaskTemplateFactory.create_batch(size=2)
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        # Act
        global_constants_interactor.\
            create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )

        #Assert
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants = GlobalConstant.objects.all()

        counter = 1
        for global_constant in global_constants:
            snapshot.assert_match(
                global_constant.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                global_constant.name, f'constant_name_{counter}'
            )
            snapshot.assert_match(
                global_constant.value, f'value_{counter}'
            )
            counter = counter + 1


    @pytest.mark.django_db
    def test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data(
            self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "TEMPLATE_ID-0"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        TaskTemplateFactory.create_batch(size=2)

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.create_batch(
            size=1, task_template_id=template_id, name="Constant_0"
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.constants_custom_exceptions import ExistingGlobalConstantNamesNotInGivenData

        # Assert
        with pytest.raises(ExistingGlobalConstantNamesNotInGivenData) as err:
            global_constants_interactor.\
                create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )

        snapshot.assert_match(err.value.args[0], 'message')

        from ib_tasks.models.global_constant import GlobalConstant
        global_constants = GlobalConstant.objects.all()

        counter = 1
        for global_constant in global_constants:
            snapshot.assert_match(
                global_constant.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                global_constant.name, f'constant_name_{counter}'
            )
            snapshot.assert_match(
                global_constant.value, f'value_{counter}'
            )
            counter = counter + 1

    @pytest.mark.django_db
    def test_with_existing_constant_but_different_configuration_updates_constant(
            self, global_constants_interactor, snapshot):
        # Arrange
        template_id = "TEMPLATE_ID-0"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        TaskTemplateFactory.create_batch(size=2)

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.create_batch(
            size=1, task_template_id=template_id, name="Constant_0"
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=1, constant_name="Constant_0", value=10000
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        # Assert
        global_constants_interactor.\
            create_global_constants_to_template_wrapper(
            global_constants_with_template_id_dto=global_constants_with_template_id_dto
        )

        from ib_tasks.models.global_constant import GlobalConstant
        global_constants = GlobalConstant.objects.all()

        counter = 1
        for global_constant in global_constants:
            snapshot.assert_match(
                global_constant.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                global_constant.name, f'constant_name_{counter}'
            )
            snapshot.assert_match(
                global_constant.value, f'value_{counter}'
            )
            counter = counter + 1
