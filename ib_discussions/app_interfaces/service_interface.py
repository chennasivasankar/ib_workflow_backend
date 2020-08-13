from ib_discussions.interactors.dtos.dtos import DiscussionWithEntityDetailsDTO


class ServiceInterface:

    @staticmethod
    def create_discussion(
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage)
        interactor.create_discussion(
            discussion_with_entity_details_dto=discussion_with_entity_details_dto
        )
