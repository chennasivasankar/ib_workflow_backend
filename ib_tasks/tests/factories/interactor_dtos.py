import factory

from ib_tasks.interactors.dtos import (
    StageActionDTO, TaskTemplateStageActionDTO,
    GoFFieldsDTO, FieldValuesDTO,
    TaskDTO
)


class StageActionDTOFactory(factory.Factory):
    class Meta:
        model = StageActionDTO

    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))
    action_name = factory.Sequence(lambda n: 'action_name_%d' % (n+1))
    logic = factory.Sequence(lambda n: 'logic%d' % (n+1))
    roles = factory.Sequence(lambda n: [f'ROLE_{n+1}', f'ROLE_{n+2}'])
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n+1))
    button_color = factory.Sequence(lambda n: 'button_color_%d' % (n+1))
    function_path = "sample_function_path"


class TaskTemplateStageActionDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStageActionDTO
    task_template_id = factory.Sequence(lambda n: "task_template_%d" % (n+1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))
    action_name = factory.Sequence(lambda n: 'action_name_%d' % (n+1))
    logic = factory.Sequence(lambda n: 'logic%d' % (n+1))
    roles = factory.Sequence(lambda n: [f'ROLE_{n+1}', f'ROLE_{n+2}'])
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n+1))
    button_color = factory.Sequence(lambda n: 'button_color_%d' % (n+1))
    function_path = "sample_function_path"
from ib_tasks.interactors.dtos import GlobalConstantsDTO


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)


class FieldValuesDTOFactory(factory.Factory):
    class Meta:
        model = FieldValuesDTO

    field_id = factory.sequence(lambda counter: "FIELD_ID-{}".format(counter))
    field_value = factory.sequence(
        lambda counter: "FIELD_VALUE-{}".format(counter)
    )


class GoFFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GoFFieldsDTO

    gof_id = factory.sequence(lambda counter: "GOF_ID-{}".format(counter))

    @factory.LazyAttribute
    def field_values_dtos(self):
        field_values_dtos = FieldValuesDTOFactory.create_batch(size=2)
        return field_values_dtos


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskDTO

    task_template_id = factory.sequence(
        lambda counter: "TASK_TEMPLATE_ID-{}".format(counter)
    )

    @factory.LazyAttribute
    def gof_fields_dtos(self):
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(size=2)
        return gof_fields_dtos
