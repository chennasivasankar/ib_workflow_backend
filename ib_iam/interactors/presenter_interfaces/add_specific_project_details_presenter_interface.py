from abc import ABC, abstractmethod


class AddSpecificProjectDetailsPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_add_specific_project_details(self):
        pass
