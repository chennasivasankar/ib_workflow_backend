import datetime


def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        execution_time = datetime.datetime.now() - start_time
        print("{} has taken {} milli seconds".format(
            func, execution_time.total_seconds() * 1000))
        return result

    return wrapper
