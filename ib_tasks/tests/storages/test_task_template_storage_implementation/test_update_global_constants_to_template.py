import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestUpdateGlobalConstantsToTemplate:

    def test_update_global_constants_to_template(self, storage):
        # Arrange
        template_id = "FIN_PR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory
        from ib_tasks.tests.factories.models import GlobalConstantFactory

        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        GlobalConstantFactory.create_batch(
            size=1, task_template_id=template_id, value=100000,
            name="Constant_1"
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=1)

        # Act
        storage.update_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

        # Assert
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objects = \
            GlobalConstant.objects.filter(task_template_id=template_id)

        assert global_constants_objects[0].task_template_id == template_id
        assert global_constants_objects[0].name == \
               global_constants_dtos[0].constant_name
        assert global_constants_objects[0].value == \
               global_constants_dtos[0].value
