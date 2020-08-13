import pytest
from mock import create_autospec

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.interactors.create_or_update_task \
    .template_gofs_fields_base_validations import \
    TemplateGoFsFieldsBaseValidationsInteractor


class TestTemplateGoFsFieldsBaseValidationsInteractor:

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        gof_storage = create_autospec(GoFStorageInterface)
        return gof_storage

    @pytest.fixture
    def create_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        create_task_storage = create_autospec(
            CreateOrUpdateTaskStorageInterface)
        return create_task_storage

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        field_storage = create_autospec(FieldsStorageInterface)
        return field_storage

    @pytest.fixture
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFFieldsDTOFactory
        GoFFieldsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            FieldValuesDTOFactory
        FieldValuesDTOFactory.reset_sequence()

    @pytest.fixture
    def gof_fields_dtos(self, reset_sequence):
        from ib_tasks.tests.factories.interactor_dtos import \
            GoFFieldsDTOFactory
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(size=4)
        return gof_fields_dtos

    @pytest.fixture
    def field_ids(self, gof_fields_dtos):
        all_field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            field_values_dtos = gof_fields_dto.field_values_dtos
            field_ids = [
                field_values_dto.field_id
                for field_values_dto in field_values_dtos
            ]
            all_field_ids += field_ids
        return all_field_ids

    @pytest.fixture
    def valid_gof_ids(self, gof_fields_dtos):
        valid_gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in gof_fields_dtos
        ]
        return valid_gof_ids

    def test_given_invalid_gof_ids_raise_exception(
            self, task_storage_mock, gof_storage_mock, field_storage_mock,
            create_task_storage_mock, storage_mock, gof_fields_dtos
    ):
        # Arrange
        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        created_by_id = "123e4567-e89b-12d3-a456-426614174000"
        task_template_id = "template1"
        action_type = ActionTypes.NO_VALIDATIONS.value
        valid_gof_ids = [gof_fields_dtos[1].gof_id, gof_fields_dtos[3].gof_id]
        invalid_gof_ids = [gof_fields_dtos[0].gof_id,
                           gof_fields_dtos[2].gof_id]
        interactor = TemplateGoFsFieldsBaseValidationsInteractor(
            gof_storage=gof_storage_mock, task_storage=task_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock
        )
        gof_storage_mock.get_existing_gof_ids.return_value = valid_gof_ids

        # Act
        with pytest.raises(InvalidGoFIds) as err:
            interactor.perform_base_validations_for_template_gofs_and_fields(
                gof_fields_dtos=gof_fields_dtos, created_by_id=created_by_id,
                task_template_id=task_template_id, action_type=action_type
            )

        # Assert
        exception_object = err.value
        assert exception_object.gof_ids == invalid_gof_ids
        gof_storage_mock.get_existing_gof_ids.assert_called_once()

    def test_given_invalid_field_ids_raise_exception(
            self, task_storage_mock, gof_storage_mock, field_storage_mock,
            create_task_storage_mock, storage_mock, gof_fields_dtos, field_ids,
            valid_gof_ids
    ):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        created_by_id = "123e4567-e89b-12d3-a456-426614174000"
        task_template_id = "template1"
        action_type = ActionTypes.NO_VALIDATIONS.value

        valid_field_ids = [
            field_ids[0], field_ids[1],
            field_ids[2], field_ids[3]
        ]
        invalid_field_ids = [
            field_ids[4], field_ids[5],
            field_ids[6], field_ids[7]
        ]
        interactor = TemplateGoFsFieldsBaseValidationsInteractor(
            gof_storage=gof_storage_mock, task_storage=task_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock
        )
        gof_storage_mock.get_existing_gof_ids.return_value = valid_gof_ids
        task_storage_mock.get_existing_field_ids.return_value = valid_field_ids

        # Act
        with pytest.raises(InvalidFieldIds) as err:
            interactor.perform_base_validations_for_template_gofs_and_fields(
                gof_fields_dtos=gof_fields_dtos, created_by_id=created_by_id,
                task_template_id=task_template_id, action_type=action_type
            )

        # Assert
        exception_object = err.value
        assert exception_object.field_ids == invalid_field_ids
        task_storage_mock.get_existing_field_ids.assert_called_once_with(
            field_ids)

    def test_given_gofs_that_are_not_related_to_given_task_template_raise_exception(
            self, task_storage_mock, gof_storage_mock, field_storage_mock,
            create_task_storage_mock, storage_mock, gof_fields_dtos, field_ids,
            valid_gof_ids
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate
        created_by_id = "123e4567-e89b-12d3-a456-426614174000"
        task_template_id = "template1"
        action_type = ActionTypes.NO_VALIDATIONS.value
        interactor = TemplateGoFsFieldsBaseValidationsInteractor(
            gof_storage=gof_storage_mock, task_storage=task_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock
        )
        valid_task_template_gof_ids = [valid_gof_ids[0], valid_gof_ids[1]]
        invalid_task_template_gof_ids = [valid_gof_ids[2], valid_gof_ids[3]]
        gof_storage_mock.get_existing_gof_ids.return_value = valid_gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        create_task_storage_mock.get_all_gof_ids_related_to_a_task_template \
            .return_value = valid_task_template_gof_ids

        # Act
        with pytest.raises(InvalidGoFsOfTaskTemplate) as err:
            interactor.perform_base_validations_for_template_gofs_and_fields(
                gof_fields_dtos=gof_fields_dtos, created_by_id=created_by_id,
                task_template_id=task_template_id, action_type=action_type
            )

        # Assert
        exception_object = err.value
        assert exception_object.gof_ids == invalid_task_template_gof_ids
        assert exception_object.task_template_id == task_template_id
        create_task_storage_mock.get_all_gof_ids_related_to_a_task_template\
            .assert_called_once_with(
            task_template_id)
