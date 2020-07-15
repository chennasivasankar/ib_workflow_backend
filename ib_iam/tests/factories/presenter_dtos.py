import factory

from ib_iam.interactors.presenter_interfaces.dtos import CompleteUserDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO


class CompleteUserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteUserDetailsDTO
    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "user%s" % number)
    email = factory.sequence(lambda number: "useremail%s@gmail.com" % number)
    teams = factory.SubFactory(UserTeamDTO)
