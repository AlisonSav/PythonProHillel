dec_list = []


def add_func(func):
    """Add function's name to the list"""
    dec_list.append(func.__name__)
    return func


@add_func
def summ(x, y):
    return x + y


@add_func
def mul(x, y):
    return x * y


print(dec_list)

