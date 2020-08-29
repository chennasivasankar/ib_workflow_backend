import mock
import pytest

from ib_tasks.interactors.add_project_to_task_templates_interactor import \
    AddProjectToTaskTemplatesInteractor


class TestAddProjectToTaskTemplatesInteractor:
    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        task_template_storage = mock.create_autospec(
            TaskTemplateStorageInterface)
        return task_template_storage

    def test_with_duplicate_template_ids_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_1"]
        expected_duplicate_task_template_ids = ["template_1"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateTaskTemplateIdsGivenToAProject

        # Assert
        with pytest.raises(DuplicateTaskTemplateIdsGivenToAProject) as err:
            interactor.add_project_to_task_templates_interactor(
                project_id=project_id, task_template_ids=task_template_ids
            )
        assert err.value.args[0] == expected_duplicate_task_template_ids

    def test_with_invalid_template_ids_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateIds

        # Assert
        with pytest.raises(InvalidTaskTemplateIds) as err:
            interactor.add_project_to_task_templates_interactor(
                project_id=project_id, task_template_ids=task_template_ids
            )
        assert err.value.args[0] == task_template_ids

    def test_with_invalid_project_id_raises_exception(
            self, task_template_storage_mock, mocker):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage_mock
        )
        task_template_storage_mock. \
            get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = task_template_ids
        from ib_tasks.tests.common_fixtures.adapters.project_service import \
            get_valid_project_ids_mock
        valid_project_ids_mock_method = get_valid_project_ids_mock(mocker)
        valid_project_ids_mock_method.return_value = []

        from ib_tasks.exceptions.custom_exceptions import InvalidProjectId

        # Assert
        with pytest.raises(InvalidProjectId) as err:
            interactor.add_project_to_task_templates_interactor(
                project_id=project_id, task_template_ids=task_template_ids
            )
        assert err.value.args[0] == project_id

    def test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates(
            self, task_template_storage_mock, mocker):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage_mock
        )
        task_template_storage_mock. \
            get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = task_template_ids
        from ib_tasks.tests.common_fixtures.adapters.project_service import \
            get_valid_project_ids_mock
        valid_project_ids_mock_method = get_valid_project_ids_mock(mocker)
        valid_project_ids_mock_method.return_value = [project_id]

        task_template_storage_mock.\
            get_existing_task_template_ids_of_project_task_templates.\
            return_value = []

        # Act
        interactor.add_project_to_task_templates_interactor(
            project_id=project_id, task_template_ids=task_template_ids
        )

        # Assert
        task_template_storage_mock.\
            get_valid_task_template_ids_in_given_task_template_ids.\
            assert_called_once_with(template_ids=task_template_ids)
        task_template_storage_mock.add_project_to_task_templates.\
            assert_called_once_with(
                project_id=project_id, task_template_ids=task_template_ids)

    def test_when_existing_task_templates_to_project_in_given_ids_then_adds_remaining_templates(
            self, task_template_storage_mock, mocker):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]
        new_template_ids_of_project = ["template_2"]
        existing_template_ids_of_project = ["template_1"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage_mock
        )
        task_template_storage_mock. \
            get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = task_template_ids
        from ib_tasks.tests.common_fixtures.adapters.project_service import \
            get_valid_project_ids_mock
        valid_project_ids_mock_method = get_valid_project_ids_mock(mocker)
        valid_project_ids_mock_method.return_value = [project_id]

        task_template_storage_mock.\
            get_existing_task_template_ids_of_project_task_templates.\
            return_value = existing_template_ids_of_project

        # Act
        interactor.add_project_to_task_templates_interactor(
            project_id=project_id, task_template_ids=task_template_ids
        )

        # Assert
        task_template_storage_mock.\
            get_valid_task_template_ids_in_given_task_template_ids.\
            assert_called_once_with(template_ids=task_template_ids)
        task_template_storage_mock.add_project_to_task_templates.\
            assert_called_once_with(
                project_id=project_id,
                task_template_ids=new_template_ids_of_project)
