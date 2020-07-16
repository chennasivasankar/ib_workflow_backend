import abc


class GetBoardsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_user_have_no_access_for_boards(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_offset(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_limit(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_boards(self, board_dtos):
        pass


class GetBoardsDetailsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_invalid_board_ids(self, error):
        pass

    @abc.abstractmethod
    def get_response_for_board_details(self, board_dtos):
        pass
