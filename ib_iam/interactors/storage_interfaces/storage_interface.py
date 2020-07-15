import abc


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_is_admin_of_given_user_id(self, user_id: int):
        pass
