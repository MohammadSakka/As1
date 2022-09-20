import time



def decorator_4(func):
    def wrapper(*args):
        wrapper.calls +=1
        t = time.time()
        try:    
            func(*args)
        except:
            print("we have an error in func ",func.__name__)
        exec_time = time.time() - t
        print(func.__name__ + " call" ,wrapper.calls, " executed in ", exec_time, " sec") 
    wrapper.calls = 0
    return wrapper

    
