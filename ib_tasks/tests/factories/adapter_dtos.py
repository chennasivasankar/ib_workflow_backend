import json

import factory

from ib_tasks.adapters.dtos import *
from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.constants.constants import STAGE_TASK
from ib_tasks.interactors.stages_dtos import EntityTypeDTO


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


class AssigneeDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AssigneeDetailsDTO

    assignee_id = factory.sequence(
            lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
                    counter))
    name = factory.sequence(lambda counter: "name_{}".format(counter))
    profile_pic_url = "https://www.google.com/search?q=ibhubs&client=ubuntu" \
                      "&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved" \
                      "=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw" \
                      "=1848&bih=913#imgrc=Kg3TRY0jmx3udM"


class UserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsDTO

    user_id = factory.Sequence(lambda n: 'user_id_%d' % (n + 1))
    user_name = factory.Sequence(lambda n: 'user_name_%d' % (n + 1))
    profile_pic_url = factory.Sequence(lambda n: 'profile_pic_%d' % (n + 1))


class EntityTypeDTOFactory(factory.Factory):
    class Meta:
        model = EntityTypeDTO

    entity_id = factory.Sequence(lambda n: n)
    entity_type = STAGE_TASK


class SearchableDetailsDTOFactory(factory.Factory):
    class Meta:
        model = SearchableDetailsDTO

    search_type = Searchable.STATE.value
    id = 2
    value = "Hyderabad"


class ProjectDetailsDTOFactory(factory.Factory):
    class Meta:
        model = ProjectDetailsDTO

    project_id = factory.sequence(lambda counter: "project{}".format(counter))
    name = factory.sequence(lambda counter: "project_name{}".format(counter))
    logo_url = factory.sequence(lambda counter: "logo_url{}".format(counter))


class TeamDetailsWithUserIdDTOFactory(factory.Factory):
    class Meta:
        model = TeamDetailsWithUserIdDTO

    user_id = factory.sequence(
            lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
                    counter))
    team_id = factory.sequence(lambda counter: "team_{}".format(counter))
    name = factory.sequence(lambda counter: "team_name{}".format(counter))


class TeamInfoDTOFactory(factory.Factory):
    class Meta:
        model = TeamInfoDTO

    team_id = factory.Sequence(lambda counter: "team_{}".format(counter))
    team_name = factory.Sequence(lambda counter: "team_name{}".format(counter))


class TeamDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TeamDetailsDTO

    team_id = factory.Sequence(lambda counter: "team_{}".format(counter))
    name = factory.Sequence(lambda counter: "team_name{}".format(counter))


class UserIdWIthTeamDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UserIdWIthTeamDetailsDTOs

    user_id = factory.sequence(
            lambda counter: "123e4567-e89b-12d3-a456-42661417400{}".format(
                    counter))

    @factory.lazy_attribute
    def team_details(self):
        return TeamDetailsDTOFactory.create_batch(size=2)


class UserSearchableDetailsDTOFactory(factory.Factory):
    class Meta:
        model = SearchableDetailsDTO

    search_type = Searchable.USER.value
    id = factory.Sequence(lambda n: "123e4567-e89b-12d3-a456-42661417400%d"
                                    % n)
    value = factory.Sequence(lambda n: json.dumps({
            "name": "User%d",
            "profile_pic_url": "https:ew.com"
    }) % n)


class UserProjectStatusDTOFactory(factory.Factory):

    class Meta:
        model = UserProjectStatusDTO

    user_id = factory.Sequence(lambda counter: "user_{}".format(counter))
    project_id = factory.Sequence(lambda counter: "project_{}".format(counter))
    is_exists = True

class TaskBoardsDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskBoardsDetailsDTO

    board_dto = factory.SubFactory(BoardDTOFactory)

    @factory.lazy_attribute
    def column_stage_dtos(self):
        return [ColumnStageDTOFactory(), ColumnStageDTOFactory()]

    @factory.lazy_attribute
    def columns_dtos(self):
        return [ColumnDTOFactory(), ColumnDTOFactory()]
