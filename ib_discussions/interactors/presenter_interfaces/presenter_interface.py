from abc import ABC, abstractmethod

from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsDetailsDTO


class CreateDiscussionPresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_entity_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        pass

    @abstractmethod
    def prepare_success_response_for_create_discussion(self):
        pass


class GetDiscussionsPresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_entity_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass

    @abstractmethod
    def prepare_response_for_discussions_details_dto(
            self, discussions_details_dto: DiscussionsDetailsDTO
    ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass
