import abc


class PopulateScriptPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_board_id(self, err):
        pass