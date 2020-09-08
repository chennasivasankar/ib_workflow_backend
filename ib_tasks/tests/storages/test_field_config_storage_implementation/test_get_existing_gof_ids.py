import pytest

from ib_tasks.tests.factories.models import GoFFactory


@pytest.mark.django_db
class TestGetExistingGoFIds:

    def test_get_existing_gof_ids_given_gof_ids(self, gof_storage):
        # Arrange
        gof_ids = ["gof0", "gof1", "gof2"]
        GoFFactory(gof_id="gof0")
        GoFFactory(gof_id="gof1")
        expected_existing_gof_ids = ["gof0", "gof1"]

        # Act
        actual_existing_gof_ids = gof_storage.get_existing_gof_ids(gof_ids)

        # Assert

        assert expected_existing_gof_ids == actual_existing_gof_ids
