import factory

from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    TaskWithCompleteStageDetailsDTO
from ib_tasks.tests.factories.interactor_dtos import \
    StageAssigneeDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import ActionDetailsDTOFactory, \
    FieldDetailsDTOFactory, StageAssigneeDTOFactory


class TaskIdWithStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithStageDetailsDTO

    task_id = factory.Sequence(lambda n: 'task_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    stage_display_name = factory.Sequence(
        lambda n: 'stage_display_%d' % (n + 1))
    stage_color = factory.sequence(lambda n: "color_{}".format(n + 1))
    db_stage_id = factory.Sequence(lambda n: n + 1)


class TaskWithCompleteStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskWithCompleteStageDetailsDTO
    task_with_stage_details_dto = \
        factory.SubFactory(TaskIdWithStageDetailsDTOFactory)
    stage_assignee_dto = \
        factory.SubFactory(StageAssigneeDetailsDTOFactory)


class GetTaskStageCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskStageCompleteDetailsDTO

    task_id = factory.Sequence(lambda n: 'task_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    field_dtos = None
    action_dtos = None
