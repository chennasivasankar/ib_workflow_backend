import factory

from ib_utility_tools.constants.enum import EntityType, TimerEntityType
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithEntityDTO, ChecklistItemWithChecklistIdDTO, EntityDTO, \
    ChecklistItemWithIdDTO, TimerEntityDTO, TimerDetailsDTO


class EntityDTOFactory(factory.Factory):
    class Meta:
        model = EntityDTO

    entity_id = factory.Faker("uuid4")
    entity_type = EntityType.TASK.value


class ChecklistItemWithEntityDTOFactory(EntityDTOFactory, factory.Factory):
    class Meta:
        model = ChecklistItemWithEntityDTO

    text = factory.sequence(lambda number: "text%s" % number)
    is_checked = False


class ChecklistItemWithChecklistIdDTOFactory(factory.Factory):
    class Meta:
        model = ChecklistItemWithChecklistIdDTO

    checklist_id = factory.Faker("uuid4")
    text = factory.sequence(lambda number: "text%s" % number)
    is_checked = False


class ChecklistItemWithIdDTOFactory(factory.Factory):
    class Meta:
        model = ChecklistItemWithIdDTO

    checklist_item_id = factory.Faker("uuid4")
    text = factory.sequence(lambda number: "text%s" % number)
    is_checked = False


class TimerEntityDTOFactory(factory.Factory):
    class Meta:
        model = TimerEntityDTO

    entity_id = factory.Faker("uuid4")
    entity_type = TimerEntityType.STAGE_TASK.value


class TimerDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TimerDetailsDTO

    duration_in_seconds = factory.Iterator([100, 300, 500])
    is_running = False
