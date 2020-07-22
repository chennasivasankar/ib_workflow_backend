import factory

from ib_tasks.interactors.dtos import (
    TaskTemplateStageActionDTO, StageActionDTO, FieldDisplayDTO
)
from ib_tasks.interactors.dtos import GlobalConstantsDTO


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


class FieldDisplayDTOFactory(factory.Factory):

    class Meta:
        model = FieldDisplayDTO

    field_id = factory.Sequence(lambda n: 'field_%d' % (n + 1))
    field_type = factory.Sequence(lambda n: 'field_type_%d' % (n + 1))
    key = factory.Sequence(lambda n: 'key_%d' % (n + 1))
    value = factory.Sequence(lambda n: 'value_%d' % (n + 1))


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)
