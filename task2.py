import time
import inspect


def decorator_2(func):
    def wrapper(*args,**kwargs):
        wrapper.calls +=1
        t = time.time()
        func(*args,**kwargs)
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
        print("Name: ",func.__name__)
        print("Type: ",type(func))
        print("Sign: " ,inspect.signature(func))
        print("Args: ", "positional ", args, "\n", "\tkey=worded ", kwargs)
        print("Doc: " ,func.__doc__)
        print("Source: " ,inspect.getsource(func))
        

    wrapper.calls = 0
    return wrapper

