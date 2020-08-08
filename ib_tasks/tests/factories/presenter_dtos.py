import factory
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO
from ib_tasks.tests.factories.storage_dtos import ActionDetailsDTOFactory, \
    FieldDetailsDTOFactory


class TaskIdWithStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithStageDetailsDTO

    task_id = factory.Sequence(lambda n: 'task_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    stage_display_name = factory.Sequence(
        lambda n: 'stage_display_%d' % (n + 1))
    stage_color = factory.sequence(lambda n: "color_{}".format(n + 1))


class GetTaskStageCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskStageCompleteDetailsDTO

    task_id = factory.Sequence(lambda n: 'task_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    field_dtos = None
    action_dtos = None
