from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()

        execution_time[fn.__name__] = end - start

        return result

        
    return wrapper



@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b


# print(func_add(3, 4))
# print(execution_time)
