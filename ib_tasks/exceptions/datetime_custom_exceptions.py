import datetime


class StartDateIsAheadOfDueDate(Exception):

    def __init__(
            self, given_start_date: datetime.date,
            given_due_date: datetime.date
    ):
        self.given_due_date = given_due_date
        self.given_start_date = given_start_date


class DueDateIsBehindStartDate(Exception):

    def __init__(
            self, given_due_date: datetime.date,
            given_start_date: datetime.date
    ):
        self.given_start_date = given_start_date
        self.given_due_date = given_due_date


class InvalidDueTimeFormat(Exception):

    def __init__(self, given_due_time: str):
        self.due_time = given_due_time


class DueTimeHasExpiredForToday(Exception):

    def __init__(self, given_due_time: str):
        self.due_time = given_due_time


class DueDateHasExpired(Exception):

    def __init__(self, given_due_date: datetime.date):
        self.due_date = given_due_date
