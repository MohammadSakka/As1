import time
from datetime import datetime


def decorator_4(func):
    def wrapper(*args):
        wrapper.calls +=1
        t = time.time()
        try:    
            func(*args)
        except Exception as err:
            with open("log.txt", "a") as log:
                log.write(f"Timestamp: {datetime.now().timestamp()}\n")
                log.write(f"We have an error in {func.__name__}\n")
                log.write(f"Error: {err}\n")
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
    wrapper.calls = 0
    return wrapper

    
