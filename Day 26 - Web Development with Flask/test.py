import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        final_time = time.time() - current_time
        print(f"{function.__name__} run speed: {final_time}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(100000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()