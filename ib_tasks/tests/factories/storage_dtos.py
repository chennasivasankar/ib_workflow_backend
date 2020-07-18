import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    StageDTO, TaskStagesDTO)


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Iterator([-1, 1, 2, 3, 4, 5, 0, 6])
    stage_display_name = factory.Sequence(lambda n: 'stage_display_name_%d' % n)
    stage_display_logic = factory.Sequence(lambda n: 'Value[stage%d]==Value[other_stage]' % n)


class TaskStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
