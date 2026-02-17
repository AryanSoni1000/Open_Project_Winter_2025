import time

def measure_runtime(function, *args):
    start = time.time()
    result = function(*args)
    end = time.time()
    return result, end - start

