import uuid

import factory

from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserCompanyDTO, UserRoleDTO, UserDTO, TeamDTO, \
    CompanyDTO, RoleDTO


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    is_admin = True
    company_id = factory.sequence(lambda number: "company%s" % number)


class UserTeamDTOFactory(factory.Factory):
    class Meta:
        model = UserTeamDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    team_id = factory.sequence(lambda number: "team%s" % number)
    team_name = factory.sequence(lambda number: "team %s" % number)


class UserCompanyDTOFactory(factory.Factory):
    class Meta:
        model = UserCompanyDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    company_id = factory.sequence(lambda number: "company%s" % number)
    company_name = factory.sequence(lambda number: "company %s" % number)


class UserRoleDTOFactory(factory.Factory):
    class Meta:
        model = UserRoleDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    name = factory.Sequence(lambda n: 'payment %s' % n)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)


class TeamDTOFactory(factory.Factory):
    class Meta:
        model = TeamDTO

    team_id = factory.sequence(lambda number: "team%s" % number)
    team_name = factory.sequence(lambda number: "team %s" % number)

class CompanyDTOFactory(factory.Factory):
    class Meta:
        model = CompanyDTO

    company_id = factory.Sequence(lambda n: 'Company%s' % n)
    company_name = factory.Sequence(lambda n: 'company %s' % n)

class RoleDTOFactory(factory.Factory):
    class Meta:
        model = RoleDTO

    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    name = factory.Sequence(lambda n: 'payment%s' % n)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)
