def trace(func):
    """This decorator prints information for called function"""

    def inner(*args, **kwargs):
        """Inner doc"""
        print(f'name = {func.__name__}, args = {args}, kwargs = {kwargs}')
        return func(*args, **kwargs)

    return inner


@trace
def some_func(x, y, key='value'):
    """This function doesn't do something useful"""
    return x, y, key


some_func(10, 15, key="alis")
