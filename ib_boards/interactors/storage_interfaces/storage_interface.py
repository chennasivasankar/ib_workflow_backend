import abc


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_board_id(self, board_id):
        pass
