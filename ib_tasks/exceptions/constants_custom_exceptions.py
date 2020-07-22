from typing import List


class InvalidOrderValues(Exception):

    def __init__(self, invalid_order_values: List[int]):
        self.order_values = invalid_order_values


class ExistingGlobalConstantNamesNotInGivenData(Exception):
    def __int__(self, message: str):
        self.message = message


class DuplicateConstantNames(Exception):
    def __int__(self, message: str):
        self.message = message


class InvalidTypeForOrder(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidTypeForValue(Exception):
    def __init__(self, message: str):
        self.message = message
