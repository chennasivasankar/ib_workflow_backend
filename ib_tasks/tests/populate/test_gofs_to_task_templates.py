import pytest
from ib_tasks.tests.factories.interactor_dtos import \
    GoFWithOrderAndAddAnotherDTOFactory
from ib_tasks.interactors.dtos import GoFsWithTemplateIdDTO

class TestGoFsToTaskTemplate:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory
        GoFFactory.reset_sequence()
        GoFWithOrderAndAddAnotherDTOFactory.reset_sequence()
        GoFWithOrderAndAddAnotherDTOFactory.enable_add_another_gof.reset()
        TaskTemplateFactory.reset_sequence()

    @pytest.fixture
    def gofs_to_task_template_interactor(self):
        from ib_tasks.interactors.add_gofs_to_task_template_interactor \
            import AddGoFsToTaskTemplateInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation

        task_storage = TasksStorageImplementation()
        gofs_to_task_template_interactor = AddGoFsToTaskTemplateInteractor(
            task_storage=task_storage
        )
        return gofs_to_task_template_interactor

    @pytest.mark.django_db
    def test_with_invalid_template_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        #Arrange
        template_id = "FIN_MAN"
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)

        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            TemplateDoesNotExists

        #Asssert
        with pytest.raises(TemplateDoesNotExists) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_template_id_is_empty_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=" ", gof_dtos=gof_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_gof_id_is_empty_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, gof_id=" "
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_invalid_value_for_order_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=-3
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidOrdersForGoFs

        # Assert
        with pytest.raises(InvalidOrdersForGoFs) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_duplicate_gof_ids_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, gof_id="gof_1"
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import DuplicateGoFIds

        # Assert
        with pytest.raises(DuplicateGoFIds) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_duplicate_values_for_orders_of_gof_ids_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=1
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateOrderValuesForGoFs

        # Assert
        with pytest.raises(DuplicateOrderValuesForGoFs) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_when_given_invalid_gofs_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            GofsDoesNotExist

        # Assert
        with pytest.raises(GofsDoesNotExist) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_valid_data(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)
        from ib_tasks.tests.factories.models import GoFFactory
        GoFFactory.create_batch(size=2)
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )

        #Act
        gofs_to_task_template_interactor.add_gofs_to_task_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

        #Assert
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gofs_to_task_template_objs = TaskTemplateGoFs.objects.all()

        counter = 1
        for gofs_to_task_template_obj in gofs_to_task_template_objs:
            snapshot.assert_match(
                gofs_to_task_template_obj.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.gof_id, f'gof_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.order, f'order_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.enable_add_another_gof,
                f'enable_add_another_gof_{counter}'
            )
            counter = counter + 1

    @pytest.mark.django_db
    def test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        import factory
        template_id = "template_1"
        from ib_tasks.tests.factories.models import \
            TaskTemplateWith2GoFsFactory
        TaskTemplateWith2GoFsFactory(template_id=template_id)
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=factory.Iterator([4, 5]), enable_add_another_gof=True
        )

        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )

        #Act
        gofs_to_task_template_interactor.add_gofs_to_task_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

        #Assert
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gofs_to_task_template_objs = TaskTemplateGoFs.objects.all()

        counter = 1
        for gofs_to_task_template_obj in gofs_to_task_template_objs:
            snapshot.assert_match(
                gofs_to_task_template_obj.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.gof_id, f'gof_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.order, f'order_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.enable_add_another_gof,
                f'enable_add_another_gof_{counter}'
            )
            counter = counter + 1

    @pytest.mark.django_db
    def test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception(
            self, gofs_to_task_template_interactor, snapshot):
        # Arrange
        template_id = "template_1"
        from ib_tasks.tests.factories.models import \
            TaskTemplateWith2GoFsFactory
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=1, order=2, enable_add_another_gof=True
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTO(
            template_id=template_id, gof_dtos=gof_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGoFsNotInGivenData

        #Assert
        with pytest.raises(ExistingGoFsNotInGivenData) as err:
            gofs_to_task_template_interactor.\
                add_gofs_to_task_template_wrapper(
                    gofs_with_template_id_dto=gofs_with_template_id_dto
                )
        snapshot.assert_match(err.value.args[0], 'message')
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gofs_to_task_template_objs = TaskTemplateGoFs.objects.all()

        counter = 1
        for gofs_to_task_template_obj in gofs_to_task_template_objs:
            snapshot.assert_match(
                gofs_to_task_template_obj.task_template_id,
                f'task_template_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.gof_id, f'gof_id_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.order, f'order_{counter}'
            )
            snapshot.assert_match(
                gofs_to_task_template_obj.enable_add_another_gof,
                f'enable_add_another_gof_{counter}'
            )
            counter = counter + 1
