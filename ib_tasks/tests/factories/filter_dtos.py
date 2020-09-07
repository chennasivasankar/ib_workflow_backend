"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
import factory

from ib_tasks.constants.constants import VALID_FIELD_TYPES
from ib_tasks.constants.enum import Operators
from ib_tasks.interactors.filter_dtos import FilterDTO, \
    CreateConditionDTO, CreateFilterDTO, ConditionDTO, UpdateFilterDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldTypeDTO


class FilterDTOFactory(factory.Factory):
    class Meta:
        model = FilterDTO

    filter_id = factory.sequence(lambda n: "field_{}".format(n))
    filter_name = factory.sequence(lambda n: "filed_name_{}".format(n))
    user_id = factory.sequence(lambda n: "{}".format(n))
    is_selected = False
    template_id = factory.sequence(lambda n: "template_{}".format(n))
    template_name = factory.sequence(lambda n: "template_name_{}".format(n))


class ConditionDTOFactory(factory.Factory):
    class Meta:
        model = ConditionDTO

    filter_id = factory.sequence(lambda n: "filter_{}".format(n))
    condition_id = factory.sequence(lambda n: "condition_{}".format(n))
    field_id = factory.sequence(lambda n: "field_{}".format(n))
    field_name = factory.sequence(lambda n: "field_name{}".format(n))
    operator = Operators.GTE.value
    value = factory.sequence(lambda n: "value_{}".format(n))


class CreateFilterDTOFactory(factory.Factory):
    class Meta:
        model = CreateFilterDTO

    filter_name = factory.sequence(lambda n: "filed_name_{}".format(n))
    user_id = factory.sequence(lambda n: "{}".format(n))
    template_id = factory.sequence(lambda n: "template_{}".format(n))
    project_id = factory.sequence(lambda n: "project_{}".format(n))


class UpdateFilterDTOFactory(factory.Factory):
    class Meta:
        model = UpdateFilterDTO

    filter_id = factory.sequence(lambda n: "{}".format(n + 1))
    filter_name = factory.sequence(lambda n: "filed_name_{}".format(n))
    user_id = factory.sequence(lambda n: "{}".format(n))
    template_id = factory.sequence(lambda n: "template_{}".format(n))


class CreateConditionDTOFactory(factory.Factory):
    class Meta:
        model = CreateConditionDTO

    field_id = factory.sequence(lambda n: "field_{}".format(n))
    operator = Operators.EQ.value
    value = factory.sequence(lambda n: "value_{}".format(n))


class FieldTypeDTOFactory(factory.Factory):
    class Meta:
        model = FieldTypeDTO

    field_id = factory.Sequence(lambda counter: "field_{}".format(counter))
    field_type = factory.Iterator(VALID_FIELD_TYPES)
