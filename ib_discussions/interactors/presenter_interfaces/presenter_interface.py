from abc import ABC, abstractmethod


class PresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_entity_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        pass

    @abstractmethod
    def prepare_success_response_for_create_discussion(self):
        pass
