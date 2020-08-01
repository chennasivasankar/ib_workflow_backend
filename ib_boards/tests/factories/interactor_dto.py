import factory

from ib_boards.interactors.dtos import ColumnTasksDTO


class TaskColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnTasksDTO

    column_id = factory.Sequence(lambda n: "column_id_%d" % n)
    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
