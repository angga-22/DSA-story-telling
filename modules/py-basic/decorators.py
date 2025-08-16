import time

# why wrapper function is required, because we only want that this decorator only runs whenever the base function being invoked. 
# not when it is initialized
def measure_time(func):
    # args = when we want to pass any number of arguments, will be treated as tuple args[0]
    # kwargs = when we want to pass positional arguments, will be treated as dictionary
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
    return wrapper


def greeting(func):
    def wrapper(*args, **kwargs):
        print('Hello,')
        func(*args, **kwargs)
    return wrapper

@greeting
@measure_time
def morning(name):
    print(f"Good morning, {name}!")


morning("angga ganteng")



