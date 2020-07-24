import factory


from ib_boards.interactors.dtos import TaskDTO, TaskDetailsDTO, FieldsDTO, TaskStageDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    TaskFieldsDTO, TaskActionsDTO, ColumnDetailsDTO, BoardDTO, TaskBoardsDetailsDTO, ColumnBoardDTO)


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)

class TaskStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskDetailsDTO

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
            button_color=factory.Sequence(lambda n: "a%df1fd" % n)
        )


class TaskFieldsDTOFactory(factory.Factory):
    class Meta:
        model = TaskFieldsDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    field_type = factory.Sequence(lambda n: "field_type_%d" % n)
    key = factory.Sequence(lambda n: "key_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)


class ColumnDetailsDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDetailsDTO

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    name = factory.Sequence(
        lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')

class FieldsDTOFactory(factory.Factory):
    class Meta:
        model = FieldsDTO

    task_template_id = factory.Sequence(lambda n: "task_template_id%d" % n)
    field_id = factory.Sequence(lambda n: "field_id_%d" % n)


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')

