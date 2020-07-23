
from unittest.mock import create_autospec
from ib_tasks.interactors.get_gofs_and_status_variables_to_task \
    import GetGroupOfFieldsAndStatusVariablesToTaskInteractor
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class TestGetGroupOfFieldsAndStatusVariablesToTaskInteractor:

    @staticmethod
    def test_given_invalid_task_id_raises_exception():
        # Arrange
        task_id = "task_1"
        storage = create_autospec(StorageInterface)
        storage.validate_task_id.return_value = False
        interactor = GetGroupOfFieldsAndStatusVariablesToTaskInteractor(
            storage=storage
        )
        import pytest

        # Act
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
        with pytest.raises(InvalidTaskIdException) as error:
            interactor.get_gofs_and_status_variables_to_task(task_id=task_id)

        # Assert
        assert error.value.task_id == task_id

    @staticmethod
    def test_given_valid_task_id_returns_task_gof_st_variables_dto():
        # Arrange
        task_id = "task_1"
        storage = create_autospec(StorageInterface)
        storage.validate_task_id.return_value = True
        from ib_tasks.tests.factories.storage_dtos import (
            FieldValueDTOFactory, StatusVariableDTOFactory,
            GroupOfFieldsDTOFactory
        )
        GroupOfFieldsDTOFactory.reset_sequence()
        FieldValueDTOFactory.reset_sequence()
        StatusVariableDTOFactory.reset_sequence()
        group_of_fields = [GroupOfFieldsDTOFactory()]
        fields = [FieldValueDTOFactory()]
        statuses = [StatusVariableDTOFactory()]
        storage.get_task_group_of_fields_dto.return_value = group_of_fields
        storage.get_fields_to_group_of_field_ids.return_value = fields
        storage.get_status_variables_to_task.return_value = statuses
        interactor = GetGroupOfFieldsAndStatusVariablesToTaskInteractor(
            storage=storage
        )
        from ib_tasks.interactors.gofs_dtos import TaskGofAndStatusesDTO

        expected_task_dto = TaskGofAndStatusesDTO(
            task_id="task_1",
            group_of_fields_dto=group_of_fields,
            fields_dto=fields,
            statuses_dto=statuses
        )

        # Act
        response_dto = interactor.get_gofs_and_status_variables_to_task(
            task_id=task_id
        )

        # Assert
        assert response_dto == expected_task_dto

