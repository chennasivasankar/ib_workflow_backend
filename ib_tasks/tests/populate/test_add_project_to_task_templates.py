import factory
import pytest

from ib_tasks.interactors.add_project_to_task_templates_interactor import \
    AddProjectToTaskTemplatesInteractor
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    ProjectTaskTemplateFactory


@pytest.mark.django_db
class TestAddProjectToTaskTemplatesInteractor:
    @pytest.fixture
    def task_template_storage(self):
        from ib_tasks.storages.task_template_storage_implementation import \
            TaskTemplateStorageImplementation
        task_template_storage = TaskTemplateStorageImplementation()
        return task_template_storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence(1)

    def test_with_duplicate_template_ids_raises_exception(
            self, task_template_storage):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_1"]
        expected_duplicate_task_template_ids = ["template_1"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage
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
            self, task_template_storage):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage
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
            self, task_template_storage, mocker):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]
        TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage
        )

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
            self, task_template_storage, mocker, snapshot):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]
        TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage
        )

        from ib_tasks.tests.common_fixtures.adapters.project_service import \
            get_valid_project_ids_mock
        valid_project_ids_mock_method = get_valid_project_ids_mock(mocker)
        valid_project_ids_mock_method.return_value = [project_id]

        # Act
        interactor.add_project_to_task_templates_interactor(
            project_id=project_id, task_template_ids=task_template_ids
        )

        # Assert
        from ib_tasks.models import ProjectTaskTemplate
        project_task_templates = ProjectTaskTemplate.objects.filter(
            project_id=project_id, task_template_id__in=task_template_ids
        )

        counter = 1
        for project_task_template in project_task_templates:
            snapshot.assert_match(
                project_task_template.id,
                'project_task_template_id_of_project_task_template_{}'.\
                    format(counter))
            snapshot.assert_match(
                project_task_template.project_id,
                'project_id_of_project_task_template_{}'.format(counter))
            snapshot.assert_match(
                project_task_template.task_template_id,
                'task_template_id_of_project_task_template_{}'.format(counter))
            counter = counter + 1

    def test_when_existing_task_templates_to_project_in_given_ids_then_adds_remaining_templates(
            self, task_template_storage, mocker, snapshot):
        # Arrange
        project_id = "CCBP"
        task_template_ids = ["template_1", "template_2"]
        new_template_ids_of_project = ["template_2"]
        existing_template_ids_of_project = ["template_1"]

        TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))
        ProjectTaskTemplateFactory.create(
            task_template_id=
            factory.Iterator(existing_template_ids_of_project),
            project_id=project_id
        )

        interactor = AddProjectToTaskTemplatesInteractor(
            task_template_storage=task_template_storage
        )

        from ib_tasks.tests.common_fixtures.adapters.project_service import \
            get_valid_project_ids_mock
        valid_project_ids_mock_method = get_valid_project_ids_mock(mocker)
        valid_project_ids_mock_method.return_value = project_id

        # Act
        interactor.add_project_to_task_templates_interactor(
            project_id=project_id, task_template_ids=task_template_ids
        )

        # Assert
        from ib_tasks.models import ProjectTaskTemplate
        new_project_task_template = ProjectTaskTemplate.objects.get(
            project_id=project_id,
            task_template_id__in=new_template_ids_of_project
        )
        snapshot.assert_match(
            new_project_task_template.id,
            'project_task_template_id_of_new_project_task_template')
        snapshot.assert_match(
            new_project_task_template.project_id,
            'project_id_of_new_project_task_template')
        snapshot.assert_match(
            new_project_task_template.task_template_id,
            'task_template_id_of_new_project_task_template_1')
