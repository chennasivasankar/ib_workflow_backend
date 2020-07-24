import pytest
from unittest.mock import create_autospec, patch
from ib_tasks.interactors.get_task_interactor \
    import GetTaskInteractor
from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor


class TestTaskInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface\
            import GetTaskPresenterInterface
        presenter = create_autospec(GetTaskPresenterInterface)
        return presenter

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

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
    def gof_ids(self):
        gof_ids = ["gof0", "gof1", "gof2"]
        return gof_ids

    @pytest.fixture
    def permission_gof_ids(self):
        permission_gof_ids = ["gof0", "gof1"]
        return permission_gof_ids

    @pytest.fixture
    def permission_task_gof_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFDTOFactory
        permission_task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
        ]
        return permission_task_gof_dtos

    @pytest.fixture
    def task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0", field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field1", field_response="response1"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2", field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3", field_response="response3"),
            TaskGoFFieldDTOFactory(task_gof_id=2, field_id="field4", field_response="response4")
        ]
        return task_gof_field_dtos

    @pytest.fixture
    def field_ids(self):
        field_ids = ["field0", "field1", "field2", "field3"]
        return field_ids

    @pytest.fixture
    def permission_field_ids(self):
        permission_field_ids = ["field0", "field2", "field3"]
        return permission_field_ids

    @pytest.fixture
    def permission_task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        permission_task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0", field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2", field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3", field_response="response3")
        ]
        return permission_task_gof_field_dtos

    @pytest.fixture
    def task_details_dto(self, task_gof_dtos, task_gof_field_dtos):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            template_id="template0",
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def permission_task_details_dto(
            self, permission_task_gof_dtos, permission_task_gof_field_dtos
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            template_id="template0",
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=permission_task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def user_roles(self):
        user_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
        return user_roles

    @pytest.fixture
    def task_complete_details_dto(self, permission_task_details_dto):
        from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
            import TaskCompleteDetailsDTO
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_id="task0",
            task_details_dto=permission_task_details_dto
        )
        return task_complete_details_dto

    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_invalid_task_id_raise_exception(
            self, get_task_mock, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        user_id = "user1"
        task_id = "task0"
        exception_object = InvalidTaskIdException(task_id)
        get_task_mock.side_effect = exception_object
        interactor = GetTaskInteractor(storage=storage_mock)
        presenter_mock.raise_exception_for_invalid_task_id.return_value = mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_id=task_id, presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_task_id.\
            assert_called_once_with(exception_object)

    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_returns_task_details_dto(
            self, get_task_mock, mocker, storage_mock, presenter_mock, task_details_dto
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        user_id = "user1"
        task_id = "task0"
        get_task_mock.return_value = task_details_dto
        interactor = GetTaskInteractor(storage=storage_mock)

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_id=task_id, presenter=presenter_mock
        )

        # Assert
        get_user_role_ids_mock_method.assert_called_once()

    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_returns_task_complete_details_dto(
            self, get_task_mock, mocker, storage_mock, presenter_mock,
            task_details_dto, user_roles, gof_ids, permission_gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            permission_task_gof_field_dtos, task_complete_details_dto,
            mock_object

    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)

        user_id = "user1"
        task_id = "task0"
        get_task_mock.return_value = task_details_dto
        interactor = GetTaskInteractor(storage=storage_mock)
        storage_mock.get_gof_ids_having_permission.return_value = permission_gof_ids
        storage_mock.get_field_ids_having_permission.return_value = permission_field_ids
        presenter_mock.get_task_response.return_value = mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_id=task_id, presenter=presenter_mock
        )
        # Assert
        get_user_role_ids_mock_method.assert_called_once()
        storage_mock.get_gof_ids_having_permission.assert_called_once_with(
            gof_ids, user_roles
        )
        storage_mock.get_field_ids_having_permission.assert_called_once_with(field_ids, user_roles)
        presenter_mock.get_task_response.assert_called_once_with(task_complete_details_dto)

