class MaxColumnsCantBeEmpty(Exception):
    pass


class MaxColumnsMustBeANumber(Exception):

    def __init__(self, invalid_max_column_value: str):
        self.max_column = invalid_max_column_value


class MaxColumnsMustBeAPositiveInteger(Exception):

    def __init__(self, invalid_max_column_value: str):
        self.max_column = invalid_max_column_value
