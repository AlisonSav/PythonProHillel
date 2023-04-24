def decorator_with_arguments(mom, dad):
    """There is a decorator with arguments"""

    def decorator(func):
        def function(son, daughter):
            print('There are decorators arguments and functions arguments. All family: ', mom, dad, son, daughter)
            return func(son, daughter)

        return function

    return decorator


@decorator_with_arguments('Mom', 'Dad')
def new_func(arg1, arg2):
    print(f'There are children: {arg1}, {arg2}')


new_func('Son', 'Daughter')
