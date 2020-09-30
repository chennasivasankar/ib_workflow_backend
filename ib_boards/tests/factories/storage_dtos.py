import factory

from ib_boards.constants.enum import DisplayStatus
from ib_boards.interactors.dtos import GetTaskDetailsDTO, TaskDetailsDTO, \
    FieldsDTO, ActionDTO, FieldDTO, TaskStageDTO
from ib_boards.interactors.storage_interfaces.dtos import (
    ColumnDetailsDTO, BoardDTO,
    ColumnCompleteDetails)
from ib_boards.interactors.storage_interfaces.storage_interface import \
    FieldDisplayStatusDTO, FieldOrderDTO


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskDetailsDTO

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
        model = ActionDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    action_id = factory.Sequence(lambda n: "action_id_%d" % n)
    action_type = factory.Sequence(lambda n: "action_type_%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)
    button_text = factory.Sequence(lambda n: "button_text_%d" % n)
    button_color = None
    transition_template_id = factory.Sequence(lambda n: "template_%d" % n)

    class Params:
        factory.Trait(
            button_color=factory.Sequence(lambda n: "a%df1fd" % n)
        )


class TaskStageDTOFactory(factory.Factory):
    class Meta:
        model = TaskStageDTO

    task_id = factory.Sequence(lambda n: n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    db_stage_id = factory.Sequence(lambda n: n)
    display_name = "stage"
    stage_color = factory.Iterator(["blue", "orange", "green"])


class TaskFieldsDTOFactory(factory.Factory):
    class Meta:
        model = FieldDTO

    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    field_id = factory.Sequence(lambda n: "field_id_%d" % n)
    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    field_type = factory.Sequence(lambda n: "field_type_%d" % n)
    key = factory.Sequence(lambda n: "key_%d" % n)
    value = factory.Sequence(lambda n: "value_%d" % n)


class ColumnCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = ColumnCompleteDetails

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    name = factory.Sequence(
        lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    total_tasks = 1


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


class FieldDisplayStatusDTOFactory(factory.Factory):
    class Meta:
        model = FieldDisplayStatusDTO

    display_status = DisplayStatus.SHOW.value
    field_id = factory.Sequence(lambda n: "field_id_%d" % n)


class FieldOrderDTOFactory(factory.Factory):
    class Meta:
        model = FieldOrderDTO

    order = factory.Sequence(lambda n: n)
    field_id = factory.Sequence(lambda n: "field_id_%d" % n)
