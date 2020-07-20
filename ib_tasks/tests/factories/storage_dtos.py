import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStatusDTO, StageDTO, ValidStageDTO, TaskStagesDTO)


class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    status_variable_id = factory.Sequence(lambda n: 'status_id_%d' % n)


class StageDTOFactory(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Sequence(lambda n: n)
    id = None
    stage_display_name = factory.Sequence(lambda n: 'name_%d' % n)
    stage_display_logic = factory.Sequence(lambda n: 'status_id_%d==stage_id' % n)

    class Params:
        id_value = factory.Trait(id=factory.Sequence(lambda n: n))


class ValidStageDTOFactory(factory.Factory):
    class Meta:
        model = ValidStageDTO

    id = factory.Sequence(lambda n: (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)


class TaskStageDTOFactory(factory.Factory):
    class Meta:
        model = TaskStagesDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
