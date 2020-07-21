import factory
from ib_tasks.interactors.dtos import GlobalConstantsDTO, TaskDTO, \
    GoFFieldsDTO, FieldValuesDTO


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)


class FieldValuesDTOFactory(factory.Factory):
    class Meta:
        model = FieldValuesDTO

    field_id = factory.sequence(lambda counter: "FIELD_ID-{}".format(counter))
    field_value = factory.sequence(
        lambda counter: "FIELD_VALUE-{}".format(counter)
    )


class GoFFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GoFFieldsDTO

    gof_id = factory.sequence(lambda counter: "GOF_ID-{}".format(counter))

    @factory.LazyAttribute
    def field_values_dtos(self):
        field_values_dtos = FieldValuesDTOFactory.create_batch(size=2)
        return field_values_dtos


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskDTO

    task_template_id = factory.sequence(
        lambda counter: "TASK_TEMPLATE_ID-{}".format(counter)
    )

    @factory.LazyAttribute
    def gof_fields_dtos(self):
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(size=2)
        return gof_fields_dtos
