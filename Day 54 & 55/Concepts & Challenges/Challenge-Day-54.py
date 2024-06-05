import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970



def speed_calc_decorator(function):
    def wrapper_function():
        before = time.time()
        function()
        after = time.time()
        execution_time = after - before
        print(f"{function.__name__} run speed: {execution_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
