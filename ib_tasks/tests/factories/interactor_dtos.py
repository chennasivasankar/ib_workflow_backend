import factory
from ib_tasks.interactors.dtos import GlobalConstantsDTO, StagesActionDTO


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
