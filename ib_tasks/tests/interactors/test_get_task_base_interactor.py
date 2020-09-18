import pytest

from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor


class TestGetTaskBaseInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def gof_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        storage = create_autospec(GoFStorageInterface)
        return storage

    @pytest.fixture
    def reset_sequence(self):
        from ib_tasks.tests.factories.storage_dtos import TaskGoFDTOFactory
        TaskGoFDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.storage_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.storage_dtos import \
            TaskGoFFieldDTOFactory
        TaskGoFFieldDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.adapter_dtos import \
            ProjectDetailsDTOFactory
        ProjectDetailsDTOFactory.reset_sequence()

    def test_given_invalid_task_id_raise_exception(
            self, storage_mock, gof_storage_mock
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        task_id = "task0"
        interactor = GetTaskBaseInteractor(
            storage=storage_mock,
            gof_storage=gof_storage_mock
        )
        storage_mock.validate_task_id.side_effect = InvalidTaskIdException(
            task_id)

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            interactor.get_task(task_id=task_id)

        # Assert
        assert str(err.value) == task_id
        storage_mock.validate_task_id.assert_called_once_with(task_id=task_id)

    def test_given_valid_task_id_returns_task_details_dto(
            self, storage_mock, gof_storage_mock,
            mocker, reset_sequence
    ):
        # Arrange
        from ib_tasks.tests.factories.adapter_dtos import \
            ProjectDetailsDTOFactory
        from ib_tasks.tests.factories.storage_dtos import \
            TaskGoFFieldDTOFactory
        from ib_tasks.tests.factories.storage_dtos import TaskDetailsDTOFactory
        from ib_tasks.tests.factories.storage_dtos import TaskGoFDTOFactory
        from ib_tasks.tests.factories.storage_dtos import \
            TaskBaseDetailsDTOFactory
        import factory
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_project_info_for_given_ids_mock
        get_projects_info_for_given_ids_mock_method = \
            get_project_info_for_given_ids_mock(
                mocker)
        ProjectDetailsDTOFactory.reset_sequence()
        task_gof_dtos = TaskGoFDTOFactory.create_batch(size=3)
        project_details_dto = ProjectDetailsDTOFactory()
        project_id = project_details_dto.project_id
        task_base_details_dto = TaskBaseDetailsDTOFactory(project_id=project_id)
        task_id = "task0"
        task_gof_ids = [
            task_gof_dto.task_gof_id
            for task_gof_dto in task_gof_dtos
        ]
        gof_ids = [
            task_gof_dto.gof_id
            for task_gof_dto in task_gof_dtos
        ]
        interactor = GetTaskBaseInteractor(
            storage=storage_mock,
            gof_storage=gof_storage_mock
        )
        task_gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(
            size=5,  task_gof_id=factory.Iterator(task_gof_ids)
        )
        task_details_dto = TaskDetailsDTOFactory(
            task_base_details_dto=task_base_details_dto,
            project_details_dto=project_details_dto,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        storage_mock.validate_task_id.return_value = task_base_details_dto
        storage_mock.get_task_gof_dtos.return_value = task_gof_dtos
        storage_mock.get_task_gof_field_dtos.return_value = task_gof_field_dtos
        gof_storage_mock.get_gof_ids_for_given_template.return_value = gof_ids

        # Act
        response = interactor.get_task(task_id=task_id)

        # Assert
        assert response == task_details_dto
        storage_mock.validate_task_id.assert_called_once_with(task_id=task_id)
        storage_mock.get_task_gof_dtos.assert_called_once_with(
            task_id=task_id,
            gof_ids=gof_ids
        )
        storage_mock.get_task_gof_field_dtos.assert_called_once_with(
            task_gof_ids=task_gof_ids)
        get_projects_info_for_given_ids_mock_method.assert_called_once()
