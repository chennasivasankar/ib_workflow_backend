import uuid

import factory

from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserCompanyDTO, UserRoleDTO


class UserTeamDTOFactory(factory.Factory):
    class Meta:
        model = UserTeamDTO

    user_id = factory.Iterator(["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013b8"])
    team_id = factory.Iterator(["ef91fdfe-bc40-444c-84e2-01f02a8d96c2",
                                "ef91fdfe-bc40-444c-84e2-01f02a8d96c3",
                                'ef91fdfe-bc40-444c-84e2-01f02a8d96c4'])
    team_name = factory.sequence(lambda number: "team %s" % number)


class UserCompanyDTOFactory(factory.Factory):
    class Meta:
        model = UserCompanyDTO

    user_id = factory.Iterator(["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013b8"])
    company_id = factory.LazyFunction(uuid.uuid4)
    company_name = factory.sequence(lambda number: "company %s" % number)


class UserRoleDTOFactory(factory.Factory):
    class Meta:
        model = UserRoleDTO

    user_id = factory.Iterator(["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                                "dd67ab82-ab8a-4253-98ae-bef82b8013b8"])
    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    role_name = factory.Sequence(lambda n: 'payment %s' % n)
    role_description = factory.Sequence(lambda n: 'payment_description%s' % n)
