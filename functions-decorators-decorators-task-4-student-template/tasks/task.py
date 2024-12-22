import functools
def decorator_apply(func):
    '''
    Add your implementation here
    '''
    def decorator(original_func):

        def wrapper(*args, **kwargs):
            return_lambda = func(args[0])
            new_args = (return_lambda,) + args[1:]
            return original_func(*new_args, **kwargs)

        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

return_user_id(42) 