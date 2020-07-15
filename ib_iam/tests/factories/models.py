import uuid

import factory


class TeamFactory(factory.Factory):
    team_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "team %s" % number)


class CompanyFactory(factory.Factory):
    company_id = factory.LazyFunction(uuid.uuid4)
    name = factory.sequence(lambda number: "company %s" % number)


class RoleFactory(factory.Factory):
    role_id = factory.sequence(lambda number: "ROLE_%s" % number)
    name = factory.sequence(lambda number: "role %s" % number)
    role_description = factory.Sequence(lambda n: 'payment_description%s' % n)
