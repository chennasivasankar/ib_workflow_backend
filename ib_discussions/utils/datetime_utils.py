def get_datetime_as_string(datetime_object):
    from ib_discussions.constants.config import DATE_TIME_FORMAT
    datetime_str = datetime_object.strftime(DATE_TIME_FORMAT)
    return datetime_str
