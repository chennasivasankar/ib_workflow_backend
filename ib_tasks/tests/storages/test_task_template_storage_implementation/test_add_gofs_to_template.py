import pytest


@pytest.mark.django_db
class TestAddGoFsToTemplate:

    def test_add_gofs_to_template(self, storage):
        # Arrange
        template_id = "FIN_VENDOR"
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        TaskTemplateFactory(template_id=template_id)

        from ib_tasks.tests.factories.models import GoFFactory
        GoFFactory.create_batch(size=2)

        from ib_tasks.tests.factories.interactor_dtos import \
            GoFWithOrderAndAddAnotherDTOFactory
        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)

        # Act
        storage.add_gofs_to_template(
            template_id=template_id, gof_dtos=gof_dtos
        )

        # Assert
        from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
        gof_to_task_template_objects = \
            TaskTemplateGoFs.objects.filter(task_template_id=template_id)

        assert gof_to_task_template_objects[0].task_template_id == template_id
        assert gof_to_task_template_objects[0].gof_id == \
               gof_dtos[0].gof_id
        assert gof_to_task_template_objects[0].order == \
               gof_dtos[0].order
        assert gof_to_task_template_objects[0].enable_add_another_gof == \
               gof_dtos[0].enable_add_another_gof
        assert gof_to_task_template_objects[1].task_template_id == template_id
        assert gof_to_task_template_objects[1].gof_id == \
               gof_dtos[1].gof_id
        assert gof_to_task_template_objects[1].order == \
               gof_dtos[1].order
        assert gof_to_task_template_objects[1].enable_add_another_gof == \
               gof_dtos[1].enable_add_another_gof
