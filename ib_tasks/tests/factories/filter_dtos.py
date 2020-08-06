"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
import factory

from ib_tasks.constants.enum import Operators
from ib_tasks.interactors.filter_dtos import FilterDTO, FilterConditionDTO, \
    CreateConditionDTO, CreateFilterDTO


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
        model = FilterConditionDTO

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


class CreateConditionDTOFactory(factory.Factory):
    class Meta:
        model = CreateConditionDTO

    field_id = factory.sequence(lambda n: "field_{}".format(n))
    operator = Operators.GTE.value
    value = factory.sequence(lambda n: "value_{}".format(n))