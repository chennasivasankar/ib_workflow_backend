import factory

from ib_adhoc_tasks.interactors.dtos import GroupByInfoKanbanViewDTO, \
    OffsetLimitDTO


class OffsetLimitDTOFactory(factory.Factory):
    class Meta:
        model = OffsetLimitDTO

    offset = factory.sequence(lambda counter: counter)
    limit = factory.sequence(lambda counter: counter + 1)


class GroupByInfoKanbanViewDTOFactory(factory.Factory):
    class Meta:
        model = GroupByInfoKanbanViewDTO

    project_id = factory.sequence(lambda counter: "project_{}".format(counter))
    user_id = factory.sequence((lambda counter: "user_{}".format(counter)))

    @factory.lazy_attribute
    def task_offset_limit_dto(self):
        return OffsetLimitDTOFactory()

    @factory.lazy_attribute
    def group1_offset_limit_dto(self):
        return OffsetLimitDTOFactory()

    @factory.lazy_attribute
    def group2_offset_limit_dto(self):
        return OffsetLimitDTOFactory()
