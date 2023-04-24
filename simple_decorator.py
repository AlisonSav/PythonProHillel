def decorator_with_arguments(dec_arg_1, dec_arg_2):
    """There is a decorator with arguments"""
    def decorator(func):
        def function(func_arg_1, func_arg_2):
            print(f'There are decorators arguments and functions arguments', dec_arg_1, dec_arg_2, func_arg_1, func_arg_2)
            return func(func_arg_1, func_arg_2)

        return function

    return decorator


@decorator_with_arguments('Name_1', 'Name_2')
def new_func(arg1, arg2):
    print(f'There are only functions arguments {arg1}, {arg2}')


new_func('Arg_1', 'Arg_2')
