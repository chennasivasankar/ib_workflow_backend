import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    FieldValueDTO, StatusVariableDTO, GroupOfFieldsDTO
)


class FieldValueDTOFactory(factory.Factory):
    class Meta:
        model = FieldValueDTO

    database_id = factory.Sequence(lambda n: 'database_%d' % (n+1))
    gof_database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n+1))
    field_id = factory.Sequence(lambda n: 'field_%d' % (n+1))
    value = factory.Sequence(lambda n: 'value_%d' % (n+1))


class StatusVariableDTOFactory(factory.Factory):
    class Meta:
        model = StatusVariableDTO
    status_id = factory.Sequence(lambda n: 'status_%d' % (n+1))
    status_variable = factory.Sequence(lambda n: 'status_variable_%d' % (n+1))
    value = factory.Sequence(lambda n: 'value_%d' % (n+1))


class GroupOfFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GroupOfFieldsDTO
    database_id = factory.Sequence(lambda n: 'gof_database_%d' % (n+1))
    group_of_field_id = factory.Sequence(lambda n: 'group_of_field_%d' % (n+1))
