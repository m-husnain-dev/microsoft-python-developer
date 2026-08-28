import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds to run.")
        return result
    return wrapper

@timer
def heavy_calculation():
    sum(range(10000000))

heavy_calculation()