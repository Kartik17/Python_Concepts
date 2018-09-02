# Author: Kartik Sah
# Year: 2018
# Topic: Decorators
#  Decorators are a way to dynamically alter the functionality of your functions.

def decorator_func(use_func):
    import logging
    import time

    logging.basicConfig(filename='{}.log'.format(use_func.__name__), level = logging.INFO)

    def wrapper_func(*args,**kwargs):
        time_start = time.time()
        result = use_func(*args)
        for i in range(100000):
            a = 0
        time_end = time.time()
        delta_time = time_end - time_start
        logging.info('Ran with args: {} and kwargs: {}, time taken to complete: {delta_time:.2f} seconds'.format(args,kwargs,delta_time))
        return result


    return wrapper_func

@decorator_func
def check_func(name):
    return 'My name is ' + name

# check_func = decorator_func(check_func) -- is equivalent to @decorator_func
# check_func() now calls the wrapper_func, which takes 'Kartik' as an argument

print(check_func('Kartik'))
