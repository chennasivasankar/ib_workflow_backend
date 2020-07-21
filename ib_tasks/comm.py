from ib_tasks.interactors.storage_interfaces.storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.create_or_update_stages import CreateOrUpdateStagesInterface
from ib_tasks.tests.factories.storage_dtos import StageDTOFactory

dtos = StageDTOFactory.create_batch(size=10)

interactor = CreateOrUpdateStagesInterface(stage_storage=TaskStorageInterface)
