import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestCreateGlobalConstantsToTemplate:

    def test_create_global_constants_to_template(self, storage):
        # Arrange

        template_id = "FIN_PR"
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory

        TaskTemplateFactory.create_batch(size=1, template_id=template_id)
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)

        # Act
        storage.create_global_constants_to_template(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

        # Assert
        from ib_tasks.models.global_constant import GlobalConstant
        global_constants_objs = \
            GlobalConstant.objects.filter(task_template_id=template_id)

        assert global_constants_objs[0].task_template_id == template_id
        assert global_constants_objs[0].name == \
               global_constants_dtos[0].constant_name
        assert global_constants_objs[0].value == \
               global_constants_dtos[0].value
        assert global_constants_objs[1].task_template_id == template_id
        assert global_constants_objs[1].name == \
               global_constants_dtos[1].constant_name
        assert global_constants_objs[1].value == \
               global_constants_dtos[1].value
