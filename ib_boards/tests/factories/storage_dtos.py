import factory
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskStageDTO, TaskFieldsDTO)

class TaskStageDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)

class TaskFieldsDTOFactory(factory.Factory):
    class Meta:
        model = TaskFieldsDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    field_type = factory.Sequence(lambda n: "field_type_%d" % n)
    key = factory.Sequence(lambda n: "key_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)