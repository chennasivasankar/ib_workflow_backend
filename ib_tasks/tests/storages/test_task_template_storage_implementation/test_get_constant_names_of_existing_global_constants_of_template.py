import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestGetConstantNamesOfExistingGlobalConstantsOfTemplate:

    def test_get_constant_names_of_existing_global_constants_of_template_returns_constant_names(
            self, storage):
        # Arrange
        template_id = "FIN_PR"
        task_template = TaskTemplateFactory(template_id=template_id)
        expected_constant_names = ['constant_1', 'constant_2', 'constant_3']

        from ib_tasks.tests.factories.models import GlobalConstantFactory
        GlobalConstantFactory.create_batch(
            size=3, task_template=task_template
        )

        # Act
        global_constants_of_template = storage. \
            get_constant_names_of_existing_global_constants_of_template(
            template_id=template_id
        )

        # Assert
        assert global_constants_of_template == expected_constant_names

    def test_get_constant_names_of_existing_global_constants_of_template_when_no_constants_returns_empty_list(
            self, storage):
        # Arrange
        template_id = "template_1"
        TaskTemplateFactory(template_id=template_id)

        # Act
        global_constants_of_template = storage. \
            get_constant_names_of_existing_global_constants_of_template(
            template_id=template_id
        )

        # Assert
        assert global_constants_of_template == []
