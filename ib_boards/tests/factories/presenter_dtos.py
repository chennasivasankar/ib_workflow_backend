import factory

from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    TaskDisplayIdDTO


class TaskDisplayIdDTOFactory(factory.Factory):
    class Meta:
        model = TaskDisplayIdDTO

    task_id = factory.Sequence(lambda n: n)
    display_id = factory.Sequence(lambda n: "task_id_%d" % n)
