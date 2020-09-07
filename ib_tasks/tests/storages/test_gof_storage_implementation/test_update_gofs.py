import pytest


@pytest.mark.django_db
class TestUpdateGoFs:

    def test_update_gofs(self, storage):
        # Arrange
        from ib_tasks.models.gof import GoF
        from ib_tasks.tests.factories.storage_dtos import GoFDTOFactory
        from ib_tasks.tests.factories.models import GoFFactory
        gofs = GoFFactory.create_batch(size=2)

        gof_dtos = [
            GoFDTOFactory(
                gof_id=gofs[0].gof_id,
                gof_display_name="details of request",
                max_columns=12
            ),
            GoFDTOFactory(
                gof_id=gofs[1].gof_id,
                gof_display_name="details of vendor",
                max_columns=12
            )
        ]

        # Act
        storage.update_gofs(gof_dtos=gof_dtos)

        # Assert
        for gof_dto in gof_dtos:
            gof = GoF.objects.get(pk=gof_dto.gof_id)
            assert gof.display_name == gof_dto.gof_display_name
            assert gof.max_columns == gof_dto.max_columns
