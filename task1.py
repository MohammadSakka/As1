import io
import time
from contextlib import redirect_stdout


def decorator_1(func):
    def wrapper(*args, **kwargs):
        wrapper.calls +=1
        t = time.time()
        # Perhaps, it's useful to use contextlib for redirect stdout here, because if your test function contains print() 
        # it will be printed to console, but we don't want it
        with redirect_stdout(io.StringIO()) as output:
            result = func(*args, **kwargs)
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
        # It's better to return result of the function, because otherwise you cannot get the result of the function.
        return result 

    wrapper.calls = 0
    return wrapper

    
