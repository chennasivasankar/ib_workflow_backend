from abc import ABC, abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_discussions_not_found(self):
        pass
