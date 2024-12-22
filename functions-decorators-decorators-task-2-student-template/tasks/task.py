import time
import inspect

def log(fn):
    """
    Декоратор для логирования времени выполнения и параметров функции
    """
    
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        res = end_time - start_time

        sig = inspect.signature(fn)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()  

        positional_args = ', '.join(f'{k}={v}' for k, v in bound_args.arguments.items()
                                    if sig.parameters[k].kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD) and k not in kwargs)

        kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())

        with open('log.txt', 'w') as f:
            f.write(
                f"{fn.__name__}; args: {positional_args}; kwargs: {kwargs_str}; execution time: {round(res, 2)} sec."
            )
        return result

    return wrapper

@log
def foo(a, b, c):
    return a, b, c

print(foo(1, 2, c=3))
