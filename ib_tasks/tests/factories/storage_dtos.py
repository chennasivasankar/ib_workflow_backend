import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    TaskStatusDTO, StageDTO)

class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    status_variable_id = factory.Sequence(lambda n: 'status_variable_id_%d' % n)

class StageDTO(factory.Factory):
    class Meta:
        model = StageDTO

    stage_id = factory.Sequence(lambda n: 'stage_id_%d' % n)
    task_template_id = factory.Sequence(lambda n: 'task_template_id_%d' % n)
    value = factory.Sequence(lambda n: '%d' % n)
    stage_display_name = factory.Sequence(lambda n: 'stage_display_name_%d' % n)
    stage_display_logic = factory.Sequence(lambda n: 'Value[stage%d]==Value[other_stage%d]' % n)
