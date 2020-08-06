
import factory
from ib_tasks.adapters.dtos import *
from ib_tasks.adapters.dtos import AssigneeDetailsDTO


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: 'board__%d' % (n+1))
    name = factory.Sequence(lambda n: 'name_%d' % (n+1))


class ColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDTO
    column_id = factory.Sequence(lambda n: 'column_%d' % (n+1))
    board_id = factory.Sequence(lambda n: 'board_%d' % (n+1))
    name = factory.Sequence(lambda n: 'name_%d' % (n+1))


class ColumnStageDTOFactory(factory.Factory):
    class Meta:
        model = ColumnStageDTO
    column_id = factory.Sequence(lambda n: 'column_%d' % (n+1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n+1))


class ColumnFieldDTOFactory(factory.Factory):
    class Meta:
        model = ColumnFieldDTO
    column_id = factory.Sequence(lambda n: 'column_%d' % (n+1))
    field_ids = factory.Sequence(lambda n: [f"field_{n+1}", f"field_{n+3}"])


class AssigneeDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AssigneeDetailsDTO
    id = factory.sequence(lambda counter: "assignee_{}".format(counter))
    name = factory.sequence(lambda counter: "name_{}".format(counter))
    profile_pic = "https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM"
