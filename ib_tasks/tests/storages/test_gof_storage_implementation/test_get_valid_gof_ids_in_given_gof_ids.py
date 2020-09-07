import pytest

from ib_tasks.tests.factories.models import TaskTemplateWith2GoFsFactory


@pytest.mark.django_db
class TestGetValidGoFIdsInGivenGoFIds:

    def test_get_valid_gof_ids_in_given_gof_ids(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        gof_ids = ['gof_1', 'gof_3']
        expected_gof_ids = ['gof_1']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        # Act
        valid_gof_ids = \
            storage.get_valid_gof_ids_in_given_gof_ids(gof_ids=gof_ids)

        # Assert
        assert valid_gof_ids == expected_gof_ids
