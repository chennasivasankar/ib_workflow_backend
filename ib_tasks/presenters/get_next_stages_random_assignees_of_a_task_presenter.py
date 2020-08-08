import abc


class GetNextStagesRandomAssigneesOfATaskPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_invalid_task_id_exception(self, task_id: int):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_action(self, action_id: int):
        pass

    @abc.abstractmethod
    def raise_invalid_key_error(self):
        pass

    @abc.abstractmethod
    def raise_invalid_custom_logic_function_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_path_not_found_exception(self, path_name):
        pass

    @abc.abstractmethod
    def raise_invalid_method_not_found_exception(self, method_name):
        pass

    @abc.abstractmethod
    def get_next_stages_random_assignees_of_a_task_response(self,
                                                            stage_with_user_details_dtos):
        pass
