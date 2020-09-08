import pytest


@pytest.mark.django_db
class TestGetGoFDTOSForGivenGoFIds:

    def test_get_gof_dtos_for_given_gof_ids(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)
        gof_ids = [gof.gof_id for gof in gofs]

        # Act
        actual_gof_dtos = storage.get_gof_dtos_for_given_gof_ids(gof_ids)

        # Assert
        for gof_dto in actual_gof_dtos:
            for gof in gofs:
                if gof.gof_id == gof_dto.gof_id:
                    assert gof.display_name == gof_dto.gof_display_name
                    assert gof.max_columns == gof_dto.max_columns
