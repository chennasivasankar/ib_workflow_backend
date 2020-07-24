import pytest

from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor


class TestGetTaskBaseInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def task_gof_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFDTOFactory
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=0)
        ]
        return task_gof_dtos

    @pytest.fixture
    def task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0", field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field1", field_response="response1"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2", field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3", field_response="response3"),
            TaskGoFFieldDTOFactory(task_gof_id=2, field_id="field2", field_response="response3")
        ]
        return task_gof_field_dtos

    def test_given_invalid_task_id_raise_exception(
            self, storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        task_id = "task0"
        interactor = GetTaskBaseInteractor(storage=storage_mock)
        storage_mock.validate_task_id.side_effect = InvalidTaskIdException(task_id)

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            interactor.get_task(task_id=task_id)

        # Assert
        assert str(err.value) == task_id
        storage_mock.validate_task_id.assert_called_once_with(task_id=task_id)

    def test_given_valid_task_id_returns_task_details_dto(
            self, storage_mock, task_gof_dtos, task_gof_field_dtos
    ):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_id = "task0"
        template_id = "template0"
        task_gof_ids = [0, 1, 2]
        task_details_dto = TaskDetailsDTO(
            template_id=template_id,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        interactor = GetTaskBaseInteractor(storage=storage_mock)
        storage_mock.validate_task_id.return_value = template_id
        storage_mock.get_task_gof_dtos.return_value = task_gof_dtos
        storage_mock.get_task_gof_field_dtos.return_value = task_gof_field_dtos

        # Act
        response = interactor.get_task(task_id=task_id)

        # Assert
        response == task_details_dto
        storage_mock.validate_task_id.assert_called_once_with(task_id=task_id)
        storage_mock.get_task_gof_dtos.assert_called_once_with(task_id=task_id)
        storage_mock.get_task_gof_field_dtos.assert_called_once_with(task_gof_ids=task_gof_ids)