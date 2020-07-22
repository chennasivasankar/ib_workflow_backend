import factory
from ib_tasks.interactors.dtos import GlobalConstantsDTO, StagesActionDTO

from ib_tasks.interactors.dtos import (
    StageActionDTO, TaskTemplateStageActionDTO
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


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)

class ActionDTOFactory(factory.Factory):
    class Meta:
        model = StagesActionDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    action_name = factory.Sequence(lambda n: "name_%d" % n)
    function_path = "path"
    logic = factory.Sequence(lambda n: 'status_id_%d==stage_id' % n)
    roles = ['ALL_ROLES']
    button_text = "text"
    button_color = None

    class Params:
        color = factory.Trait(button_color="#ffffff")
