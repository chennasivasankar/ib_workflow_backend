import factory

from ib_boards.interactors.dtos import TaskColumnDTO


class TaskColumnDTOFactory(factory.Factory):
    class Meta:
        model = TaskColumnDTO

    column_id = factory.Sequence(lambda n: "column_id_%d" % n)
    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
