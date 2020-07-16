import factory
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskDTO, TaskActionsDTO)

class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    column_id = factory.Sequence(lambda n: "column_id_%d" % n)


class TaskActionsDTOFactory(factory.Factory):
    class Meta:
        model = TaskActionsDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    action_id = factory.Sequence(lambda n: "action_id_%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)
    button_text = factory.Sequence(lambda n: "button_text_%d" % n)
    button_color = None

    class Params:
        factory.Trait(
            button_color = factory.Sequence(lambda n: "a%df1fd" % n)
        )


class TaskFieldsDTOFactory(factory.Factory):
    class Meta:
        model = TaskFieldsDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    field_type = factory.Sequence(lambda n: "field_type_%d" % n)
    key = factory.Sequence(lambda n: "key_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)