import time



def decorator_1(func):
    def wrapper(*args):
        wrapper.calls +=1
        t = time.time()
        func(*args)
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
    wrapper.calls = 0
    return wrapper

    
