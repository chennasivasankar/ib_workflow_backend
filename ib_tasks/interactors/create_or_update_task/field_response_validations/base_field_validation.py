import abc
from typing import Optional


class BaseFieldValidation(abc.ABC):

    @abc.abstractmethod
    def validate_field_response(self) -> Optional[Exception]:
        pass
