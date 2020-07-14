import factory

from ib_tasks.interactors.dtos import ActionDto


class ActionDtoFactory(factory.Factory):
    class Meta:
        model = ActionDto

    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))
    action_name = factory.Sequence(lambda n: 'action_name_%d' % (n+1))
    logic = factory.Sequence(lambda n: 'logic%d' % (n+1))
    role = factory.Sequence(lambda n: 'ROLE_%d' % (n+1))
    button_text = factory.Sequence(lambda n: 'button_text_%d' % (n+1))
    button_color = factory.Sequence(lambda n: 'button_color_%d' % (n+1))
