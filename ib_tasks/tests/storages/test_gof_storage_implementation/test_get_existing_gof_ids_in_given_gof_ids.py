import pytest

from ib_tasks.tests.factories.models import GoFFactory


@pytest.mark.django_db
class TestGetExistingGoFIdsInGivenGoFIds:

    def test_get_existing_gof_ids_in_given_gof_ids(
            self, storage
    ):
        # Arrange
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        expected_existing_gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_existing_gof_ids = \
            storage.get_existing_gof_ids_in_given_gof_ids(
                gof_ids=gof_ids
            )

        # Assert
        assert expected_existing_gof_ids == actual_existing_gof_ids
