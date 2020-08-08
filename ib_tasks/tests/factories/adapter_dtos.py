import factory
from ib_tasks.adapters.dtos import *


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: 'board__%d' % (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))


class ColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDTO

    column_id = factory.Sequence(lambda n: 'column_%d' % (n + 1))
    board_id = factory.Sequence(lambda n: 'board_%d' % (n + 1))
    name = factory.Sequence(lambda n: 'name_%d' % (n + 1))


class ColumnStageDTOFactory(factory.Factory):
    class Meta:
        model = ColumnStageDTO

    column_id = factory.Sequence(lambda n: 'column_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))


class ColumnFieldDTOFactory(factory.Factory):
    class Meta:
        model = ColumnFieldDTO

    column_id = factory.Sequence(lambda n: 'column_%d' % (n + 1))
    field_ids = factory.Sequence(
        lambda n: [f"field_{n + 1}", f"field_{n + 3}"])


class UserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(lambda n: 'user_id_%d' % (n + 1))
    user_name = factory.Sequence(lambda n: 'user_name_%d' % (n + 1))
    profile_pic_url = factory.Sequence(lambda n: 'profile_pic_%d' % (n + 1))
